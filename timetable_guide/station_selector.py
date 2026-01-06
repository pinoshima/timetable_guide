#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import yaml
import os
from datetime import datetime
from math import radians, cos, sin, sqrt, atan2

class StationSelector(Node):
    def __init__(self):
        super().__init__('station_selector')

        pkg_share = os.path.join(os.getenv('AMENT_PREFIX_PATH').split(':')[0], 'share', 'timetable_guide')
        yaml_path = os.path.join(pkg_share, 'config', 'timetable.yaml')
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)
        self.stations = data['stations']

        self.get_logger().info(f'Stations loaded')
        self.get_logger().info('Station Selector started (auto mode)')

        self.pub = self.create_publisher(String, 'next_train', 10)

        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        current_lat = 35.66177
        current_lon = 140.0151

        nearest_station, distance = self.get_nearest_station(current_lat, current_lon)
        next_train_time = self.get_next_train(nearest_station, current_time)

        msg = f'Nearest station: {nearest_station} ({distance:.5f} km), Next train: {next_train_time}'
        self.get_logger().info(msg)
        self.pub.publish(String(data=msg))

    def get_nearest_station(self, lat, lon):
        min_distance = float('inf')
        nearest_station = None

        for name, info in self.stations.items():
            station_lat = info['lat']
            station_lon = info['lon']
            d = self.haversine(lat, lon, station_lat, station_lon)
            if d < min_distance:
                min_distance = d
                nearest_station = name

        return nearest_station, min_distance

    def get_next_train(self, station_name, current_time):
        times = self.stations[station_name]['times']
        for t in times:
            if t >= current_time:
                return t
        return times[0]

    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371.0
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        return R * c

def main(args=None):
    rclpy.init(args=args)
    node = StationSelector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
