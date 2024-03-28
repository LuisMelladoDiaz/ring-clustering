from enum import Enum
import random

from utils.cluster_generation import generate_centers, generate_radii

class Initialization(Enum):
    PREDEFINED = 1
    RANDOM = 2
    HEURISTIC = 3


def init_clusters(num_clusters, initialization, color):
    centers = []
    radii = [10,10,10]
    if initialization == Initialization.PREDEFINED:
        centers = init_centers_predefined(num_clusters)
    elif initialization == Initialization.RANDOM:
        centers = generate_centers(num_clusters)
        radii = generate_radii(num_clusters,5,30)
    elif initialization == Initialization.HEURISTIC:
        centers = init_centers_heuristic(num_clusters)
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

def init_centers_heuristic(num_clusters): #TODO
    pass

