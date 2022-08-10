import math

#Get the points in the curve with the bigger and smaller angle
def get_angle(first, middle, last):
    ang = math.degrees(math.atan2(last[1]-middle[1], last[0]-middle[0]) - math.atan2(first[1]-middle[1], first[0]-middle[0]))
    return ang + 360 if ang < 0 else ang

def get_bigger_angle(start,finish, dict_curve) -> tuple:
    max_angle = -1
    max_angle_time = 0
    min_angle = 361
    min_angle_time = 0
    for time, value in dict_curve.items():
        if time > finish[0]:
            break
        angle = get_angle(start, [time, value], finish)
        if angle < min_angle:
            min_angle = angle
            min_angle_time = time
        if angle > max_angle:
            max_angle = angle
            max_angle_time = time
    return max_angle, min_angle, max_angle_time, min_angle_time


