from cmath import inf
import math
import numpy as np

def get_distance(start, finish, point) -> float:
    """Return the distance between the point and the line defined by the start and finish points"""
    return np.linalg.norm(np.cross(finish-start, start-point))/np.linalg.norm(finish-start)


def get_bigger_distance(start,finish, dict_curve) -> tuple:
    """Get the bigger distance between the real curve and the start-finish line, absolute and relative"""
    slope = (finish[1] - finish[1])/(finish[0]-finish[0])
    
    right_dist = -inf 
    left_dist = inf
    right_dist_time = 0
    left_dist_time = 0
    for time, val in dict_curve.items():
        if time >= finish[0]:
            break
        if time < start[0]:
            continue

        dist = get_distance(start, finish, np.array([time, val]))
        # compare if its up or down from the base line
        if val < slope*(time-start[0]) + start[1]:
            dist = -dist
        if dist > right_dist:
            right_dist = dist
            right_dist_time = time
        if dist < left_dist:
            left_dist = dist
            left_dist_time = time

    #Normilize the distances to percentage of the total distance
    if right_dist > -left_dist:
        big_dist = right_dist
        big_dist_time = right_dist_time
    else:
        big_dist = -left_dist
        big_dist_time = left_dist_time

    big_dist_norm = 100 * big_dist / math.sqrt((finish[0] - start[0])**2 + (finish[1] - start[1])**2)
    print("big_dist = ", big_dist)
    print("big_dist_norm  = ", big_dist_norm)
    print("big_dist_time = ", big_dist_time)
    print("start-finish distance = ", math.sqrt((finish[0] - start[0])**2 + (finish[1] - start[1])**2))
    return big_dist, big_dist_norm,  big_dist_time
