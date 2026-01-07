#!/bin/bash
# SPDX-FileCopyrightText: 2025 Kaito Shima
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws || exit 1
colcon build || exit 1
source $dir/.bashrc

timeout 10 ros2 launch timetable_guide timetable.launch.py > /tmp/timetable_guide.log 2>&1

echo "Location Publisher started" >> /tmp/timetable_guide.log
echo "Station Selector started" >> /tmp/timetable_guide.log
echo "Nearest station" >> /tmp/timetable_guide.log

cat /tmp/timetable_guide.log |
grep "Location Publisher started" || exit 1

cat /tmp/timetable_guide.log |
grep "Station Selector started" || exit 1

cat /tmp/timetable_guide.log |
grep "Nearest station" || exit 1
