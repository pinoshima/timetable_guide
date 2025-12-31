#!/usr/bin/python3

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([

        Node(
            package='timetable_guide',
            executable='location_publisher',
            name='location_publisher',
            output='screen'
        ),

        Node(
            package='timetable_guide',
            executable='station_selector',
            name='station_selector',
            output='screen'
        ),

    ])

