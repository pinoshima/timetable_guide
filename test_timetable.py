#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Kaito Shima
# SPDX-License-Identifier: BSD-3-Clause

import os
import pytest
import launch
import launch_ros
import launch_testing.actions
from launch_testing.actions import ReadyToTest
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

PACKAGE_NAME = 'timetable_guide'

@pytest.mark.launch_test
def generate_test_description():
    """ローンチファイルを読み込んでテスト準備完了アクションを追加"""
    launch_file_path = os.path.join(
        os.path.dirname(__file__), 'launch', 'timetable.launch.py'
    )

    ld = launch.LaunchDescription([
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                launch_file_path
            )
        ),
        ReadyToTest()
    ])
    return ld

# --- テストクラス --- #
@pytest.mark.launch_test
def test_station_selector_output():
    """station_selector ノードが出力する最寄駅と次の列車時刻をチェック"""
    rclpy.init()
    node = Node('test_node')
    results = []

    def callback(msg):
        # 出力例: "Nearest station: Shinomiya (1.17 km), Next train: 15:20"
        results.append(msg.data)

    sub = node.create_subscription(String, 'station_selector_output', callback, 10)

    try:
        # 最大5秒間、結果が取得できるか待つ
        import time
        timeout = 5.0
        start = time.time()
        while not results and (time.time() - start) < timeout:
            rclpy.spin_once(node, timeout_sec=0.1)

        assert results, "station_selector からの出力が取得できませんでした"

        # 最低1回出力があることを確認
        output = results[0]
        assert "Nearest station:" in output
        assert "Next train:" in output
        print("出力確認OK:", output)

    finally:
        node.destroy_node()
        rclpy.shutdown()

