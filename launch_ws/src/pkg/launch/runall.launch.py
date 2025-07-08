from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    ld = LaunchDescription()

    node1 = Node(
        package="pkg",
        executable="one",
        name="my_one",
        output="screen",
    )

    node2 = Node(
        package="pkg",
        executable="two",
        name="my_two",
        output="screen",
    )

    node3 = Node(
        package="pkg",
        executable="three",
        name="my_three",
        output="screen",
    )

    ld.add_action(node1)
    ld.add_action(node2)
    ld.add_action(node3)

    return ld