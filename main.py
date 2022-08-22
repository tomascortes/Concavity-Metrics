#!/usr/bin/env python
# External libraries
from matplotlib import pyplot as plt
import numpy as np
import math
import sys

# Internal libraries
from data_manage.read_data import read_file, path_selector, get_verbose
from data_manage.output_data import update_excel
from ploting_functions.ploting_functions import plot_line, plot_lines_to_middle, plot_three_points
from index_obtaining.bigger_angle import get_bigger_angle, get_angle
from index_obtaining.bigger_distance import get_bigger_distance, get_distance
from index_obtaining.area import get_areas, get_triangle_area

if __name__ == "__main__":
    #Code to select the path 
    ex_path = path_selector()
    time, curve, start_x, finish_x = read_file(path=ex_path)
    if get_verbose():
        verbose = True
    else:
        verbose = input("Do you want to see the plot? (y/n) ")
        verbose = verbose == "y"
    f_x = dict(zip([round(x, 2) for x in time], curve))

    start = np.array([start_x, f_x[start_x]])
    finish = np.array([finish_x, f_x[finish_x]])
    
    ### Indexes ###
    best_distance_index = {}
    ## Pivot on bigger distance to the start-finish line ##
    # Distance
    big_dist, big_dist_norm,  big_dist_time =  get_bigger_distance(start, finish, f_x)
    best_distance_index["bigger distance"] = big_dist_time
    best_distance_index["bigger distance norm (%)"] = big_dist_norm
    best_distance_index["bigger distance time"] = big_dist_time
    best_distance_index["% time before pivot"] = 100*(big_dist_time - start[0])/(finish[0] - start[0])
    distance_point = np.array([big_dist_time, f_x[big_dist_time]])


    #Angle in bigger distance
    max_ang = get_angle(start, distance_point, finish)
    best_distance_index["angle"] = max_ang

    # Area
    upper_area, downer_area = get_areas(start, finish, f_x)
    best_distance_index["upper area"] = upper_area
    best_distance_index["downer area"] = downer_area
    best_distance_index["triangle area"] = get_triangle_area(
        start, 
        distance_point, 
        finish)
    # slopes
    best_distance_index["slope start-pivot"] = (distance_point[1] - start[1])/(distance_point[0] - start[0])
    best_distance_index["slope pivot-finish"] = (finish[1] - distance_point[1])/(finish[0] - distance_point[0])
    best_distance_index["slope start-finish"] = (finish[1] - start[1])/(finish[0] - start[0])

    ## Pivot on middle values of the data ##
    middle_distance_index = {}
    mid_time = round((start[0] + finish[0])/2, 2)
    mid_point = np.array([mid_time, f_x[mid_time]])

    # Distance
    middle_distance_index["distance"] = get_distance(start, finish, mid_point)
    middle_distance_index["distance norm (%)"] = 100*get_distance(start, finish, mid_point)/math.sqrt((finish[0] - start[0])**2 + (finish[1] - start[1])**2)
    middle_distance_index["distance time"] = mid_time
    middle_distance_index["% time before pivot"] = 100 * (mid_time - start[0]) / (finish[0] - start[0])

    # Angle in middle
    middle_distance_index["angle"] = get_angle(
        first=start, 
        middle=mid_point, 
        last=finish)

    # Triangle Area in middle
    middle_distance_index["triangle area"] = get_triangle_area(start, mid_point, finish)
    middle_distance_index["slope start-pivot"] = (mid_point[1] - start[1])/(mid_point[0] - start[0])
    middle_distance_index["slope pivot-finish"] = (finish[1] - mid_point[1])/(finish[0] - mid_point[0])

    update_excel(ex_path, best_distance_index, middle_distance_index)

    if verbose:
        # Print results big distance
        print("Bigger distance: {} at {}".format(big_dist, big_dist_time))
        print("angle: {} at {}".format(max_ang, big_dist_time))
        print("Upper area: {}".format(upper_area))
        print("Downer area: {}".format(downer_area))
        print("Triangle area: {}".format(best_distance_index["triangle area"]))

        print("-"*20)
        # Print results middle distance
        print("Middle distance: {} at {}".format(middle_distance_index["distance"], mid_time))
        print("angle: {} at {}".format(middle_distance_index["angle"], mid_time))
        print("Triangle area: {}".format(middle_distance_index["triangle area"]))
        print("Slope 1: {}".format(middle_distance_index["slope start-pivot"]))
        print("Slope 2: {}".format(middle_distance_index["slope pivot-finish"]))

        ## Ploting funcionts
        plot_line([start, finish], label="start to finish", color="orange")
        plot_three_points(start, [big_dist_time, f_x[big_dist_time]], finish, labels="Big distance", color="red")
        plt.plot(big_dist_time, f_x[big_dist_time], marker="o", markersize=5,  color="red", label="Pivot big distance")
        plt.plot(mid_time, f_x[mid_time], marker="o", markersize=5,  color="blue", label="Middle")

        #Basic graph
        plt.plot(time, curve)
        plt.axis([0, time[-1], 0, max(curve)+2])
        plt.legend()
        plt.show()
    