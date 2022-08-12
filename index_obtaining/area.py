import numpy as np
import matplotlib.pyplot as plt

def get_areas(start,finish, dict_curve) -> tuple:
    """Return the uper and downer areas of the curve"""
    slope = (start[1] - finish[1])/(start[0]-finish[0])
    line_y = lambda x: slope*(x - start[0]) + start[1]
    #Compare the first and second lower keys from the dict_curve
    dic_iter = iter(dict_curve)
    first = next(dic_iter)
    second = next(dic_iter)
    dx = second-first

    upper_area = 0
    downer_area = 0
    for time, val in dict_curve.items():
        if time > start[0] and time < finish[0]:
            dist = line_y(time) - val
            if dist > 0:
                plt.plot([time, time], [val, line_y(time)], color="green")
                upper_area += dist*dx
            else:
                plt.plot([time, time], [val, line_y(time)], color="blue")
                downer_area -= dist
    return upper_area, downer_area

def get_triangle_area(a,b,c) -> float:
    """Return the area of a triangle with sides a,b,c"""
    return abs(a*(b+c)-b*c)/2