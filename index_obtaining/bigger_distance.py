from cmath import inf
import math
import numpy as np

def get_distance(point, a, direction) -> float:
    """Return the distance between a point and a line"""
    vector = (point - a) - ((point - a).dot(direction))*direction
    return math.sqrt(vector.dot(vector))

def get_bigger_distance(start,finish, dict_curve) -> tuple:
    """Get the bigger and smaller distance between the real curve and the start-finish line"""
    # x = a + tn 
    #https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
    direction = np.array([start[0] - finish[0], start[1]-finish[1]])
    # Normilize de direction
    direction = direction / np.linalg.norm(direction)
    start = np.array([start[0], start[1]])
    finish = np.array([finish[0], finish[1]])
    vectorized_line = lambda t: start + t*direction

    big_dist = -inf 
    small_dist = inf
    big_dist_time = 0
    small_dist_time = 0
    for time, val in dict_curve.items():
        if time >= finish[0]:
            break
        if time < start[0]:
            continue
        dist = get_distance([time, val], start, direction)
        # compare if its up or down from the base line
        if val < direction[1]/direction[0]*(time-start[0]) + start[1]:
            dist = -dist
        if dist > big_dist:
            big_dist = dist
            big_dist_time = time
        if dist < small_dist:
            small_dist = dist
            small_dist_time = time

    #Normilize the distances
    big_dist = 100 * big_dist / np.linalg.norm(finish - start)
    small_dist = 100 * small_dist / np.linalg.norm(finish - start)
    return big_dist, small_dist, big_dist_time, small_dist_time
