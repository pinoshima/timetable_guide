## 時刻表案内コマンド
![test](https://github.com/pinoshima/timetable_guide/actions/workflows/test.yml/badge.svg)

## 概要
本パッケージは`location_publisher`，`station_selector`，`timetable_selector`の各ノードを提供する．

あらかじめ設定された現在地の緯度経度から最寄り駅を計算し，時刻表に基づく次の発車時刻を表示する．

## ノード、トピックの機能の説明
- `location_publisher` ノード:
  - 現在地（緯度・経度）を `/current_location` トピックにパブリッシュ

- `station_selector` ノード:
  - `/current_location` を読み込む
  - 最寄駅と次の発車時刻を計算
  - 計算結果を `/next_train` トピックにパブリッシュ

- `timetable_selector` ノード:
  - `/next_train` トピックをサブスクライブ
  - 駅名と発車時刻を受信し，表示

## 実行例
launchファイルを起動する．

`ros2 launch timetable_guide timetable.launch.py`

最寄り駅名，現在地から駅までの距離，現在の時刻から最寄り駅を出発する一番早い列車の時間を表示する．
`Nearest station: Shinomiya (1.17739 km), Next train: 17:05`

## 使用上の注意点
今回の列車の発車時刻，位置は全て架空のため，使用する際には実際の情報に書き換える必要がある．

## ライセンス
- このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます.
- © 2025 Kaito Shima
