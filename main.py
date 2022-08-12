# External libraries
from matplotlib import pyplot as plt
import numpy as np

# Internal libraries
from data_manage.read_data import read_file, path_selector
from data_manage.output_data import create_excel
from ploting_functions.ploting_functions import plot_line, plot_lines_to_middle, plot_quintiles_lines, plot_three_points
from index_obtaining.bigger_angle import get_bigger_angle, get_angle
from index_obtaining.bigger_distance import get_bigger_distance
from index_obtaining.numeric_derivate import get_numerical_second_derivative
from index_obtaining.area import get_areas, get_triangle_area

if __name__ == "__main__":
    #Code to select the path 
    ex_path = path_selector()
    time, curve = read_file(path=ex_path, work_sheet="p1")
    f_x = dict(zip([round(x, 2) for x in time], curve))

    start = np.array([0.37, 9.68])
    finish = np.array([1.29, 0.56])
    
    ### Indexes ###
    
    # Distance
    big_dist, big_dist_norm,  big_dist_time =  get_bigger_distance(start, finish, f_x)
    print("Bigger distance: {} at {}".format(big_dist, big_dist_time))
    #Angle in bigger distance
    max_ang = get_angle(start, [big_dist_time, f_x[big_dist_time]], finish)
    #Angle in smaller distance
    # area
    upper_area, downer_area = get_areas(start, finish, f_x)
    print("angle: {} at {}".format(max_ang, big_dist_time))
    print("Upper area: {}".format(upper_area))
    print("Downer area: {}".format(downer_area))

    
    ## Ploting funcionts
    #Basic line
    plot_line([start, finish], label="start to finish", color="orange")
    
    plot_three_points(start, [big_dist_time, f_x[big_dist_time]], finish, labels="Big distance", color="red")
    plt.plot(big_dist_time, f_x[big_dist_time], marker="o", markersize=5,  color="red")

    # Lines based on middle, quitniles
    # plot_quintiles_lines(start, finish, f_x)
    # plot_lines_to_middle(start, finish, f_x)


    #Basic graph
    plt.plot(time, curve)
    plt.axis([0, time[-1], 0, max(curve)+2])
    plt.legend()
    plt.show()
    