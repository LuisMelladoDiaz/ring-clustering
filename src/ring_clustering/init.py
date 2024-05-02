from enum import Enum
import random
from maths.circumcenter import circumcenter
from maths.distances import distance_point_point

from utils.cluster_generation import generate_centers, generate_radii

class Initialization(Enum):
    PREDEFINED = 1
    RANDOM = 2
    HEURISTIC = 3


def init_clusters(num_clusters, initialization, color, points):
    centers = []
    radii = [10] * num_clusters
    print(initialization)
    if initialization == Initialization.PREDEFINED:
        centers = init_centers_predefined(num_clusters)
    elif initialization == Initialization.RANDOM:
        centers = generate_centers(num_clusters)
        radii = generate_radii(num_clusters,5,30)
    elif initialization == Initialization.HEURISTIC:
        centers, radii = init_centers_heuristic(num_clusters, points)
    else:
        raise ValueError("Initialization method not recognized.")
    centers = [(x, y, color) for x, y in centers]
    return centers, radii

def init_centers_predefined(num_clusters):
    predefined_centers = [
            (10, 10), (20, 20), (30, 30), (40, 40), (50, 50),
            (60, 60), (70, 70), (80, 80), (90, 90), (25, 25),
            (50, 25), (75, 25), (25, 50), (25, 75), (50, 75),
            (75, 75), (75, 50), (90, 10), (10, 90), (90, 90)
        ]
    centers = random.sample(predefined_centers, num_clusters)
    return centers

def init_centers_heuristic(num_clusters, points):
    centers = []
    radii = []
    sorted_points = sorted(points, key=lambda point: distance_point_point(point, (0,0)))
    num_points = len(sorted_points)
    section = num_points//num_clusters

    for i in range(num_clusters):

        a = sorted_points[i*section]
        index_a = sorted_points.index(a)

        index_b = (index_a + 1) % num_points
        index_c = (index_a + 2) % num_points

        b = sorted_points[index_b]
        c = sorted_points[index_c]

        center = circumcenter(a, b, c)
        centers.append(center)
        radii.append(distance_point_point(a, center))
    return centers, radii


