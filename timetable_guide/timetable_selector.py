#!/usr/bin/python3

import rclpy
from rclpy.node import Node

import os
import yaml
from ament_index_python.packages import get_package_share_directory


class TimetableSelector(Node):

    def __init__(self):
        super().__init__('timetable_selector')

        package_share = get_package_share_directory('timetable_guide')
        config_path = os.path.join(package_share, 'config', 'timetable.yaml')

        self.get_logger().info(f'Loading timetable from: {config_path}')

        try:
            with open(config_path, 'r') as f:
                self.timetable = yaml.safe_load(f)
        except Exception as e:
            self.get_logger().error(f'Failed to load timetable.yaml: {e}')
            raise

        self.get_logger().info('Timetable loaded successfully')

def main():
    rclpy.init()
    node = TimetableSelector()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
