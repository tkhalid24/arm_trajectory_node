import math
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class ArmGroundFigure8(Node):
    def __init__(self):
        super().__init__('arm_ground_figure8')
        self.publisher_ = self.create_publisher(Int32MultiArray, 'goal_position', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.t = 0.0

        # Constants shared across motors
        self.r = 0.014
        self.get_logger().info("Ground-plane figure-8 controller with translation motor started.")

    def translation_motor(self, motor_num, alpha):
        if motor_num == 1:
            L2 = 0.042
            L3 = 0.024
            L4 = 0.039
            zeroposition = 1617
        elif motor_num == 2:
            L2 = 0.103
            L3 = 0.024
            L4 = 0.063
            zeroposition = 3131
        elif motor_num == 3:
            L2 = 0.103
            L3 = 0.024
            L4 = 0.026
            zeroposition = 1428
        else:
            self.get_logger().warn(f"Unsupported motor number: {motor_num}")
            return 2048

        # Compute motion using Law of Cosines
        L1 = math.sqrt(L3**2 + L4**2 - 2 * L3 * L4 * math.cos(abs(alpha)))
        L0 = math.sqrt(L3**2 + L4**2 - 2 * L3 * L4)
        delta_beta = (L1 - L0) / self.r

        if alpha < 0:
            delta_beta = -delta_beta

        motor_position = zeroposition + int((delta_beta / (2 * math.pi)) * 4095)

        self.get_logger().info(f"Motor {motor_num} → α: {alpha:.3f}, Δβ: {delta_beta:.4f}, L1: {L1:.4f}, Pos: {motor_position}")

        # Clamp position to valid range
        motor_position = max(0, min(4095, motor_position))
        return motor_position

    def timer_callback(self):
        A = 2  # Shoulder yaw (X movement)
        B = 3  # Elbow (Z reach)
        freq = 0.5
        t = self.t

        alpha2 = int( A * math.sin(freq * t))       # left-right
        alpha3 = int( B * math.sin(2 * freq * t))  

        # Alpha is fixed in this version
       # alpha1 = 0 * 2 * math.pi / 180
        #alpha2 = -30 * 2 * math.pi / 180
        #alpha3 = 0 * 2 * math.pi / 180 
        shoulder_pitch = 2048
        shoulder_yaw = self.translation_motor(2, alpha2)
        elbow = self.translation_motor(3, alpha3)
        wrist = 2048

        msg = Int32MultiArray()
        msg.data = [shoulder_pitch, shoulder_yaw, elbow, wrist]
        self.publisher_.publish(msg)

        self.t += 1
        if self.t > 2 * math.pi / freq:
            self.t = 0.0

def main(args=None):
    rclpy.init(args=args)
    node = ArmGroundFigure8()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

