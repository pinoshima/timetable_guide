#!/bin/bash
# SPDX-FileCopyrightText: 2025 Kaito Shima
# SPDX-License-Identifier: BSD-3-Clause

set -e

dir=~
[ "$1" != "" ] && dir="$1"

cd "$dir/ros2_ws" || exit 1

source /opt/ros/humble/setup.bash

colcon build
source install/setup.bash

export RCUTILS_LOGGING_BUFFERED_STREAM=1

timeout 10 ros2 launch timetable_guide timetable.launch.py --screen \
  > /tmp/timetable_guide.log 2>&1

cat /tmp/timetable_guide.log

grep "Location Publisher started" /tmp/timetable_guide.log
grep "Station Selector started" /tmp/timetable_guide.log
grep "Nearest station" /tmp/timetable_guide.log

