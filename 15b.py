import re
from lib.vector import Vector

pattern = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

sensors = []
distances = []
with open("15-input.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')
    for line in lines:
        matches = pattern.match(line)
        sensor_x, sensor_y, beacon_x, beacon_y = map(int, matches.groups())
        sensor = Vector(sensor_x, sensor_y)
        beacon = Vector(beacon_x, beacon_y)
        sensors.append(sensor)
        diff = beacon - sensor
        distance = abs(diff.x) + abs(diff.y)
        distances.append(distance)


def check_position(pos):
    if pos.x < 0 or 4000000 < pos.x:
        return False
    if pos.y < 0 or 4000000 < pos.y:
        return False
    for sensor_check, distance_check in zip(sensors, distances):
        diff = sensor_check - pos
        dist = abs(diff.x) + abs(diff.y)
        if dist <= distance_check:
            return False
    print(pos)
    print(pos.x * 4000000 + pos.y)
    exit()

for sensor, distance in zip(sensors, distances):
    print(sensor, sensor.y - distance - 1, sensor.y + distance + 2)
    i = 0
    for y in range(sensor.y - distance - 1, sensor.y + distance + 2):
        if y % 100000 == 0: print(y)
        pos1 = Vector(sensor.x - i, y)
        pos2 = Vector(sensor.x + i, y)
        check_position(pos1)
        check_position(pos2)
        if y >= sensor.y:
            i -= 1
        else:
            i += 1



# diff = pos - sensor
#     this_pos_distance = abs(diff.x) + abs(diff.y)
#     if this_pos_distance <= distance:
#         found = False
#         break
