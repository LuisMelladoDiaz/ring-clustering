import random
import math

from user_interface.drawing_functions import circle

def generate_points(num_points, center, radius, error=0.01):
    points = []
    for p in range(num_points):
        angle = random.uniform(0,2*math.pi)
        distance = random.uniform(radius-error,radius+error)
        x = center[0] + distance * math.cos(angle)
        y = center[1] + distance * math.sin(angle)
        points.append((x, y))
    return points

def generate_centers(num_clusters):
    centers = []
    for c in range(num_clusters):
        center = (random.uniform(0, 100), random.uniform(0, 100))
        centers.append(center)
    return centers

def generate_radii(num_clusters,min_radius,max_radius):
    radii = []
    for r in range(num_clusters):
        radius = random.uniform(min_radius, max_radius)
        radii.append(radius)
    return radii

def build_clusters(centers, radii):
    clusters = []
    for center,radius in zip(centers,radii):
        clusters.append((center,radius))
    return clusters
