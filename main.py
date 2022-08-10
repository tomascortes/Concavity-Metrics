# External libraries
from cProfile import label
from matplotlib import pyplot as plt

# Internal libraries
from data_manage.read_data import read_file, path_selector
from data_manage.output_data import create_excel
from ploting_functions.ploting_functions import plot_line, plot_lines_to_middle, plot_quintiles_lines, plot_three_points
from index_obtaining.bigger_angle import get_bigger_angle

if __name__ == "__main__":
    #Code to select the path 
    ex_path = path_selector()
    time, curve = read_file(path=ex_path, work_sheet="p1")
    f_x = dict(zip([round(x, 2) for x in time], curve))

    start = [0.37, 9.68]
    finish = [1.29, 0.56]
    max_angle, min_angle, max_angle_time, min_angle_time = get_bigger_angle(start, finish, f_x)

    
    ## Ploting funcionts
    #Basic line
    plot_line([start, finish], label="first to finish", color="blue")

    # Lines based on middle, quitniles
    # plot_quintiles_lines(start, finish, f_x)
    # plot_lines_to_middle(start, finish, f_x)

    # # Code for the min and max angle, its not good
    # plot_three_points(start, [min_angle_time, f_x[min_angle_time]], finish, labels="Min angle", color="red")
    # plt.plot(min_angle_time, f_x[min_angle_time], marker="o", markersize=5,  color="red")
    # plot_three_points(start, [max_angle_time, f_x[max_angle_time]], finish, labels="Min angle", color="green")
    # plt.plot(max_angle_time, f_x[max_angle_time], marker="o", markersize=5,  color="green")

    #Basic graph
    plt.plot(time, curve)
    plt.axis([0, time[-1], 0, max(curve)+2])
    plt.legend()
    plt.show()
    