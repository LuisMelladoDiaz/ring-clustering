import math
import random

from utils.coloring import cluster_coloring, points_coloring

def compute_membership(clusters, points):
    membership = {}
    for p in points:
        distances = {}
        for i, c in enumerate(clusters):
            distances[i] = distance_point_circle(p, c)
        sorted_clusters = sorted(distances, key=distances.get)
        membership[p] = sorted_clusters
    points = points_coloring(points, membership)
    clusters = cluster_coloring(clusters)
    return membership, points, clusters

def distance_point_circle(point, circle):
    center, radius = circle
    x,y = point
    h,k,_ = center

    distance = abs(math.sqrt((x-h)**2 + (y-k)**2)-radius)
    return distance
