import math
import numpy as np

#Get the points in the curve with the bigger and smaller angle
def get_angle(first, middle, last):
    ba = first - middle
    bc = last - middle

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)
    return np.degrees(angle)

def get_bigger_angle(start,finish, dict_curve):
    """Not usefull"""
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


