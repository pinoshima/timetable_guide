## 時刻表案内コマンド
　まだやってないよ→![test](https://github.com/pinoshima/robosys2025/actions/workflows/test.yml/badge.svg)

## 概要
`StationSelector` と `LocationPublisher` の2つのノードを提供するROS 2パッケージである．
現在地の緯度経度から最寄り駅を計算し，時刻表に基づく次の発車時刻を表示する．

## インストール方法
```bash
# ワークスペース作成
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

# リポジトリをクローン
git clone https://github.com/ユーザ名/timetable_guide.git

# ビルド
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash

## 必用なソフトウェア
- Python
  - テスト済みバージョン：3.7 ~ 3.13

## テスト環境
- Ubuntu 24.04.3 LTS
