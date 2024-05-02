from ast import literal_eval
import csv

from user_interface.drawing_functions import draw_points_and_circles
from maths.distances import compute_membership

def save_results(points, initial_clusters, clusters, title):
    filename = f'src/experiments/data/results/{title}.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y', 'color'])
        writer.writerows(points)
        writer.writerow(['center', 'radius', 'color'])
        writer.writerows(clusters)
        writer.writerow(['Initial clusters'])
        writer.writerows(initial_clusters)

def draw_experiment_result(experiment_title):
    points, clusters = parse_experiment_results(experiment_title)
    draw_points_and_circles(points,clusters,title = experiment_title)

def evaluate_new_points(new_points, experiment_title):
    points, clusters = parse_experiment_results(experiment_title)
    points.extend(new_points)
    m, c, points, clusters, e = compute_membership(clusters, points)
    draw_points_and_circles(points,clusters,title = experiment_title)

def parse_experiment_results(filename):
    filename = f'src/experiments/data/results/{filename}'
    points = []
    clusters = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        reading_points = True

        for row in reader:
            if row[0] == 'Initial clusters': break
            if row[0] == 'center': reading_points = False
            if reading_points:
                x, y = map(float, row[:2])
                color = row[2]
                points.append((x, y, color))
            elif reading_points == False and row[0] != 'center':
                center = tuple(map(float, row[0][1:-1].split(', ')))
                radius = float(row[1])
                color = literal_eval(row[2])
                clusters.append((center, radius, color))

    return points, clusters

def parse_points(points_str):
    points_str = points_str.get().strip()[1:-1]
    points_str = points_str.replace('(', '').replace(')', '').split(', ')
    parsed_points = [(float(coord.split(',')[0]), float(coord.split(',')[1])) for coord in points_str]


    return parsed_points