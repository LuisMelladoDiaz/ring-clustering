import numpy as np

def points_mean (point_list):
    parsed_point_list = []

    for p in point_list:
        x,y,*_ = p
        parsed_point_list.append((x,y))

    points_array = np.array(parsed_point_list)
    mean_x = np.mean(points_array[:, 0])
    mean_y = np.mean(points_array[:, 1])

    return (mean_x,mean_y)

