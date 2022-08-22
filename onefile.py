#!/usr/bin/env python

import contextlib as __stickytape_contextlib

@__stickytape_contextlib.contextmanager
def __stickytape_temporary_dir():
    import tempfile
    import shutil
    dir_path = tempfile.mkdtemp()
    try:
        yield dir_path
    finally:
        shutil.rmtree(dir_path)

with __stickytape_temporary_dir() as __stickytape_working_dir:
    def __stickytape_write_module(path, contents):
        import os, os.path

        def make_package(path):
            parts = path.split("/")
            partial_path = __stickytape_working_dir
            for part in parts:
                partial_path = os.path.join(partial_path, part)
                if not os.path.exists(partial_path):
                    os.mkdir(partial_path)
                    with open(os.path.join(partial_path, "__init__.py"), "wb") as f:
                        f.write(b"\n")

        make_package(os.path.dirname(path))

        full_path = os.path.join(__stickytape_working_dir, path)
        with open(full_path, "wb") as module_file:
            module_file.write(contents)

    import sys as __stickytape_sys
    __stickytape_sys.path.insert(0, __stickytape_working_dir)

    __stickytape_write_module('data_manage/read_data.py', b'import string\r\nimport os\r\nimport sys\r\nfrom openpyxl import Workbook, load_workbook\r\n\r\nclass MoreValuesThanTimeStamps(Exception):\r\n    """Raised when there are missing timestamps """\r\n    pass\r\n\r\n\r\ndef path_selector() -> string:\r\n    # Declare the dictionry options\r\n    options = dict()\r\n    counter = 1\r\n\r\n    # Print all the excel files in directory\r\n    files = os.listdir("./")\r\n    for file in files:\r\n        if ".xlsx" in file:\r\n            options[counter] = file\r\n            print(f"{counter})", end="")\r\n            print(file)\r\n            counter += 1\r\n    # Ask for input\r\n    answer = input("Write number of the file to be selected an press enter \\n")\r\n    while not answer.isdigit():\r\n        print("\\nRemember to write just a number")\r\n        answer = input("Write number of file to be selected an press enter \\n")\r\n    answer_number = int(answer)\r\n    return options[answer_number]\r\n\r\n\r\ndef read_file(path: str, work_sheet: str=None) -> tuple:\r\n    """recives a path of a excel file and return a tuple of two lists, \r\n    corresponding to time and Values"""\r\n    wb = Workbook()\r\n    wb = load_workbook(path, read_only=True, data_only=True)\r\n    if work_sheet:\r\n        ws = wb[work_sheet]\r\n    else:\r\n        ws = wb.worksheets[0]\r\n\r\n    output_time = []\r\n    output_values = []\r\n\r\n    for row in ws.rows:\r\n        output_time.append(row[0].value)\r\n        output_values.append(row[1].value)\r\n\r\n    start_x = round(ws.cell(2, 3).value, 2)\r\n    finish_x = round(ws.cell(2, 4).value, 2)\r\n\r\n\r\n    output_time.pop(0)\r\n    output_values.pop(0)\r\n\r\n    # Sometimes the data read Nones at the end,\r\n    # there should be no Nones in the middle\r\n\r\n    for i in range(len(output_time)):\r\n        if output_time[i] == None:\r\n            output_time = output_time[:i]\r\n            break\r\n\r\n    for i in range(len(output_values)):\r\n        if output_values[i] == None:\r\n            output_values = output_values[:i]\r\n            break\r\n    if len(output_values) > len(output_time):\r\n        raise MoreValuesThanTimeStamps("There are more input values than time values")\r\n    elif len(output_values) != len(output_time):\r\n        output_time = output_time[:len(output_values)]\r\n    return (output_time, output_values, start_x, finish_x)\r\n\r\ndef get_verbose() -> bool:\r\n    n = len(sys.argv)\r\n    if n >= 2:\r\n        return sys.argv[1] == "p"\r\n    return False\r\n\r\n\r\n')
    __stickytape_write_module('data_manage/output_data.py', b'from openpyxl import Workbook, load_workbook\r\nfrom openpyxl.styles import PatternFill, Font\r\n\r\n\r\ndef update_excel(path: str, big_dist_data: dict, mid_dist_data: dict):\r\n    """recives a list of lists with shape:\r\n    [integral_value, start_integral, end_integral]\r\n    and returns and creates an excel file with the data in the\r\n    output path. Creates output directory if it doesn\'t exist."""\r\n\r\n    # Create workbook\r\n    wb = Workbook()\r\n    wb = load_workbook(path, read_only=False)\r\n    ws = wb.worksheets[0]\r\n\r\n    ##General metrics##\r\n    for i, key in enumerate(["slope start-finish", "upper area", "downer area"]):\r\n        ws.cell(row=6, column=6 + i).value = key\r\n        ws.cell(row=6, column=6 + i).fill = PatternFill(start_color="75E6DA", end_color="75E6DA", fill_type = "solid")\r\n        ws.cell(row=7, column=6 + i).value = big_dist_data[key]\r\n        big_dist_data.pop(key)\r\n\r\n    # Write first set of data\r\n    title_cell = ws.cell(row=1, column=5)\r\n    title_cell.value = "Bigger Distance Pivot"\r\n    title_cell.fill = PatternFill(start_color="FF4A4A", end_color="FF4A4A", fill_type = "solid")\r\n    title_cellfont = Font(size=12)\r\n    for i, (name, value) in enumerate(big_dist_data.items()):\r\n        ws.cell(row=1, column=i+6).value = name + " BDP"\r\n        ws.cell(row=1, column=i+6).fill = PatternFill(start_color="75E6DA", end_color="75E6DA", fill_type = "solid")\r\n        ws.cell(row=2, column=i+6).value = value\r\n\r\n    \r\n\r\n    # Write second set\r\n    title_cell = ws.cell(row=3, column=5)\r\n    title_cell.value = "Middle Distance Pivot"\r\n    title_cell.fill = PatternFill(start_color="FF4A4A", end_color="FF4A4A", fill_type = "solid")\r\n    #Copied and pasted from excel file\r\n\r\n    for i, (name, value) in enumerate(mid_dist_data.items()):\r\n        ws.cell(row=3, column=i+6).value = name + " MDP"\r\n        ws.cell(row=3, column=i+6).fill = PatternFill(start_color="75E6DA", end_color="75E6DA", fill_type = "solid")\r\n        ws.cell(row=4, column=i+6).value = value\r\n\r\n    for col in ws.columns:\r\n        column = col[0].column_letter   # Get the column name\r\n        ws.column_dimensions[column].width = 20\r\n    # Save excel file\r\n    wb.save(path)\r\n\r\n\r\n')
    __stickytape_write_module('ploting_functions/ploting_functions.py', b'from matplotlib import pyplot as plt\r\n\r\ndef plot_line(points_list, label=None, color=None):\r\n    """Recives list with two points and plot the line between them"""\r\n    plt.plot([x[0] for x in points_list], [x[1] for x in points_list], label=label, color=color)\r\n\r\n\r\n\r\ndef plot_three_points(first, middle, last, labels=False, color=None):\r\n    if labels:\r\n        plot_line([first, middle], label=labels, color=color)\r\n        plot_line([middle, last], label=labels, color=color)\r\n    else:\r\n        plot_line([first, middle], color=color)\r\n        plot_line([middle, last], color=color)\r\n\r\ndef plot_quintiles_lines(start, finish, f_x):\r\n    max_time = finish[0]\r\n    colors = ["blue", "green", "orange"]\r\n    \r\n    for i in range(3):\r\n        x_time = round((i + 1)*max_time/5,2) + start[0]\r\n        plot_three_points(start, (x_time, f_x[x_time]),finish, labels=False, color=colors[i])\r\n        plt.plot(x_time, f_x[x_time], marker="o", markersize=5,  color=colors[i])\r\n\r\ndef plot_lines_to_middle(start_point, finish_point, f_x, color=None):\r\n    middle_time = round((start_point[0] + finish_point[0])/2, 2)\r\n    middle_point = [middle_time, f_x[middle_time]]\r\n    plot_three_points(start_point, middle_point, finish_point, color=color)\r\n')
    __stickytape_write_module('index_obtaining/bigger_angle.py', b'import math\r\nimport numpy as np\r\n\r\n#Get the points in the curve with the bigger and smaller angle\r\ndef get_angle(first, middle, last):\r\n    ba = first - middle\r\n    bc = last - middle\r\n\r\n    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))\r\n    angle = np.arccos(cosine_angle)\r\n    return np.degrees(angle)\r\n\r\ndef get_bigger_angle(start,finish, dict_curve):\r\n    """Not usefull"""\r\n    max_angle = -1\r\n    max_angle_time = 0\r\n    min_angle = 361\r\n    min_angle_time = 0\r\n    for time, value in dict_curve.items():\r\n        if time > finish[0]:\r\n            break\r\n        angle = get_angle(start, [time, value], finish)\r\n        if angle < min_angle:\r\n            min_angle = angle\r\n            min_angle_time = time\r\n        if angle > max_angle:\r\n            max_angle = angle\r\n            max_angle_time = time\r\n    return max_angle, min_angle, max_angle_time, min_angle_time\r\n\r\n\r\n')
    __stickytape_write_module('index_obtaining/bigger_distance.py', b'from cmath import inf\r\nimport math\r\nimport numpy as np\r\n\r\ndef get_distance(start:np.array, finish:np.array, point:np.array) -> float:\r\n    """Return the distance between the point and the line defined by the start and finish points"""\r\n    return np.linalg.norm(np.cross(finish-start, start-point))/np.linalg.norm(finish-start)\r\n\r\n\r\ndef get_bigger_distance(start,finish, dict_curve) -> tuple:\r\n    """Get the bigger distance between the real curve and the start-finish line, absolute and relative"""\r\n    slope = (finish[1] - start[1])/(finish[0]-start[0])\r\n    \r\n    right_dist = -inf \r\n    left_dist = inf\r\n    right_dist_time = 0\r\n    left_dist_time = 0\r\n    for time, val in dict_curve.items():\r\n        if time >= finish[0]:\r\n            break\r\n        if time < start[0]:\r\n            continue\r\n\r\n        dist = get_distance(start, finish, np.array([time, val]))\r\n        # compare if its up or down from the base line\r\n        if val < slope*(time-start[0]) + start[1]:\r\n            dist = -dist\r\n        if dist > right_dist:\r\n            right_dist = dist\r\n            right_dist_time = time\r\n        if dist < left_dist:\r\n            left_dist = dist\r\n            left_dist_time = time\r\n\r\n    #Normilize the distances to percentage of the total distance\r\n    if right_dist > -left_dist:\r\n        big_dist = right_dist\r\n        big_dist_time = right_dist_time\r\n    else:\r\n        big_dist = -left_dist\r\n        big_dist_time = left_dist_time\r\n\r\n    big_dist_norm = 100 * big_dist / math.sqrt((finish[0] - start[0])**2 + (finish[1] - start[1])**2)\r\n    return big_dist, big_dist_norm,  big_dist_time\r\n')
    __stickytape_write_module('index_obtaining/area.py', b'import numpy as np\r\nimport matplotlib.pyplot as plt\r\n\r\ndef get_areas(start,finish, dict_curve) -> tuple:\r\n    """Return the uper and downer areas of the curve"""\r\n    slope = (start[1] - finish[1])/(start[0]-finish[0])\r\n    line_y = lambda x: slope*(x - start[0]) + start[1]\r\n    #Compare the first and second lower keys from the dict_curve\r\n    dic_iter = iter(dict_curve)\r\n    first = next(dic_iter)\r\n    second = next(dic_iter)\r\n    dx = second-first\r\n\r\n    upper_area = 0\r\n    downer_area = 0\r\n    for time, val in dict_curve.items():\r\n        if time > start[0] and time < finish[0]:\r\n            dist = line_y(time) - val\r\n            if dist > 0:\r\n                plt.plot([time, time], [val, line_y(time)], color="green")\r\n                upper_area += dist*dx\r\n            else:\r\n                plt.plot([time, time], [val, line_y(time)], color="blue")\r\n                downer_area -= dist\r\n    return upper_area, downer_area\r\n\r\ndef get_triangle_area(a,b,c) -> float:\r\n    """Return the area of a triangle with sides a,b,c"""\r\n    return 1/2*(a[0]*(b[1] - c[1]) + b[0]*(c[1] - a[1]) + c[0]*(a[1] - b[1]))')
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
        