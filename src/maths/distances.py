import math
import random

from utils.coloring import cluster_coloring, points_coloring

def compute_membership(clusters, points):
    membership = {}
    normalized_membership_degree = {}
    error = {}
    # COMPUTE THE MEMBERSHIP OF EACH POINT
    for p in points:
        x,y,*_ = p
        distances = {}
        # DISTANCE FROM THE POINT TO THE CLUSTER
        for i, c in enumerate(clusters):
            center,radius,*_ = c
            distances[i] = distance_point_circle(p, c)

        normalized_membership_degree[p] = normalize_distances(distances)
        #print(normalized_membership_degree)
        sorted_clusters = sorted(distances, key=distances.get)
        membership[p] = sorted_clusters

        center,radius,*_ = clusters[sorted_clusters[0]]
        error[(x,y)] = abs(min(distances.values()))

    points = points_coloring(points, membership)
    clusters = cluster_coloring(clusters)

    classification = compute_classification(membership)
    return membership, classification, points, clusters, error

def compute_classification(membership):
    classification = {}
    for point, clusters in membership.items():
        closest_cluster = clusters[0]
        classification.setdefault(closest_cluster, []).append(point)
    return classification

def distance_point_circle(point, circle):
    center, radius,*_ = circle
    x,y,*_ = point
    h,k,*_ = center

    distance = abs(math.sqrt((x-h)**2 + (y-k)**2)-radius)
    return distance

def distance_point_point(pointA, pointB):
    x,y,*_ = pointA
    a,b,*_ = pointB

    distance = math.sqrt((x-a)**2 + (y-b)**2)
    return distance

def normalize_distances(distances):
    total_distance = sum(distances.values())
    if total_distance == 0:
        return {key: 0 for key in distances}
    normalized_distances = {key: value / total_distance for key, value in distances.items()}
    return normalized_distances