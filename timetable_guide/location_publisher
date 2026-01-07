#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Kaito Shima
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point


class LocationPublisher(Node):

    def __init__(self):
        super().__init__('location_publisher')

        self.publisher_ = self.create_publisher(
            Point,
            'current_location',
            10
        )

        self.timer = self.create_timer(1.0, self.publish_location)

        self.latitude = 35.66177
        self.longitude = 140.0151

        self.get_logger().info('Location Publisher started')

    def publish_location(self):
        msg = Point()
        msg.x = self.latitude
        msg.y = self.longitude
        msg.z = 0.0

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Publish location: lat={msg.x}, lon={msg.y}'
        )


def main():
    rclpy.init()
    node = LocationPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
