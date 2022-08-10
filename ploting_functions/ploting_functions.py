from matplotlib import pyplot as plt

def plot_line(points_list, label=None, color=None):
    """Recives list with two points and plot the line between them"""
    plt.plot([x[0] for x in points_list], [x[1] for x in points_list], label=label, color=color)



def plot_three_points(first, middle, last, labels=False, color=None):
    if labels:
        plot_line([first, middle], label=labels, color=color)
        plot_line([middle, last], label=labels, color=color)
    else:
        plot_line([first, middle], color=color)
        plot_line([middle, last], color=color)

def plot_quintiles_lines(start, finish, f_x):
    max_time = finish[0]
    colors = ["blue", "green", "orange"]
    
    for i in range(3):
        x_time = round((i + 1)*max_time/5,2) + start[0]
        plot_three_points(start, (x_time, f_x[x_time]),finish, labels=False, color=colors[i])
        plt.plot(x_time, f_x[x_time], marker="o", markersize=5,  color=colors[i])

def plot_lines_to_middle(start_point, finish_point, f_x, color=None):
    middle_time = round((start_point[0] + finish_point[0])/2, 2)
    middle_point = [middle_time, f_x[middle_time]]
    plot_three_points(start_point, middle_point, finish_point, color=color)
