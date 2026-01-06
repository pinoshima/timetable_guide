## 時刻表案内コマンド

## 概要
`StationSelector`と`LocationPublisher`と`timetable_selector.py`のノードを提供するパッケージである．

あらかじめ設定された現在地の緯度経度から最寄り駅を計算し，時刻表に基づく次の発車時刻を表示する．

## ノード、トピックの機能の説明
- `location_publisher` ノード:
  - 現在地（緯度・経度）を `/current_location` トピックにパブリッシュ

- `station_selector` ノード:
  - `/current_location` を読み込む
  - 最寄駅と次の発車時刻を計算
  - 計算結果を `/next_train` トピックにパブリッシュ

- `timetable_selector.py` ノード:
  - `/next_train` トピックをサブスクライブ
  - 駅名と発車時刻を受信し，表示

## 使用上の注意点
今回の列車の発車時刻，位置は全て架空のため，使用する際には実際の情報に書き換える必要がある．

## ライセンス
- このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます.
- © 2025 Kaito Shima
