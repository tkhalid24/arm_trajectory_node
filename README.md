# BioArm Figure-8 Controller (ROS 2)

This package contains a custom ROS 2 Python node that generates a figure-8 trajectory for a bio-inspired robotic arm with 4 degrees of freedom (DOF). The node mimics muscle-like joint actuation using a pulley-wire mechanism and is designed for real-time joint control using Dynamixel motors.

## 🚀 Features

- Publishes motor positions that trace a figure-8 path
- Designed for soft, compliant robotic joints using fishing line tendons
- Geometry-based control using Law of Cosines
- Modular and easily extendable
- ROS 2 (Foxy/Humble) compatible

## 🧠 System Overview

- **Motor 1**: Shoulder pitch (fixed in this node)
- **Motor 2**: Shoulder yaw (horizontal swing)
- **Motor 3**: Elbow extension (vertical reach)
- **Motor 4**: Wrist (static or extendable)

Trajectory is generated using sinusoidal angle functions mapped to motor positions via a mechanical linkage model.

Usage:
ros2 run bioarm_figure8_controller arm_ground_figure8


