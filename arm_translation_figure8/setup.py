from setuptools import setup

package_name = 'arm_translation_figure8'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='talha',
    maintainer_email='tkmirza00@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'figure8_translation_node = arm_translation_figure8.figure8_translation_node:main',
    ],


    },
)
