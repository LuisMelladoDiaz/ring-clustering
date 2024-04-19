from asyncio.windows_events import NULL
from enum import Enum
from maths import mean, distances



def check_halting(iterations, convergence, max_iterations, min_convergence):
    halt = False
    print(convergence)
    print(min_convergence)
    if (iterations >= max_iterations):
        halt = True
        print("Max iterations reached")
    if(min_convergence != NULL and convergence <= min_convergence):
        halt = True
        print("Convergence")
    return halt

def compute_convergence(old_clusters, new_clusters):
    old_centers = []
    new_centers = []
    if len(old_clusters) != len(new_clusters): return 100
    for i in range(0, len(old_clusters)):
        old_center, *_ = old_clusters[i]
        new_center, *_ = new_clusters[i]
        old_centers.append(old_center)
        new_centers.append(new_center)
    old_mean = mean.points_mean(old_centers)
    new_mean = mean.points_mean(new_centers)
    difference = distances.distance_point_point(old_mean, new_mean)
    return difference
