import re
from lib.grid import create_grid

from lib.vector import Vector

pattern = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

beacons = set()
no_beacons_positions = set()
with open("15-input.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')
    for line in lines:
        # print(line)
        matches = pattern.match(line)
        sensor_x, sensor_y, beacon_x, beacon_y = map(int, matches.groups())
        # print(sensor_x, sensor_y, beacon_x, beacon_y)
        sensor = Vector(sensor_x, sensor_y)
        beacon = Vector(beacon_x, beacon_y)
        beacons.add(beacon)
        print(sensor, beacon)
        diff = beacon - sensor
        distance = abs(diff.x) + abs(diff.y)
        print(distance)
        i = 0
        for y in range(sensor.y - distance, sensor.y + distance + 1):
            # print()
            # print("i:", i)
            if y == 2000000:
                for x in range(sensor.x - i , sensor.x + i + 1):
                    pos = Vector(x, y)
                    # print("pos: ", pos)
                    no_beacons_positions.add(pos)
            if y >= sensor.y:
                i -= 1
            else:
                i += 1
        # break


# print(no_beacons_positions)
for beacon in beacons:
    if beacon in no_beacons_positions:
        no_beacons_positions.remove(beacon)

print(len(no_beacons_positions))
# result = set()
# for item in no_beacons_positions:
#     if item.y == 2000000:
#         result.add(item)
# print(result)
# print(len(result))
