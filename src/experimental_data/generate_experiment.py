import csv
import random
import math

def generate_exp(num_points,num_clusters,min_radius=1,max_radius=20, max_error=0.05):
    centers = generate_centers(num_clusters)
    radii = generate_radius(num_clusters,min_radius,max_radius)
    error = random.uniform(0, max_error)
    points = []
    for center,radius in zip(centers,radii):
        points.extend(generate_points(num_points,center,radius,error))
    generate_csv(points)

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

def generate_radius(num_clusters,min_radius,max_radius):
    radii = []
    for r in range(num_clusters):
        radius = random.uniform(min_radius, max_radius)
        radii.append(radius)
    return radii

def generate_csv(points):
    with open('src\experimental_data\data\experiment', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y'])
        writer.writerows(points)

def parse_experiment(path='src\experimental_data\data\experiment'):
    points = []
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            points.append((float(row['x']), float(row['y'])))
    return points