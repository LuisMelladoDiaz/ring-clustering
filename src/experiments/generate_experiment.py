import csv
import random
from utils.cluster_generation import generate_centers, generate_points, generate_radii

def generate_exp(num_points,num_clusters,min_radius=1,max_radius=20, max_error=0.05,title='experiment'):
    centers = generate_centers(num_clusters)
    radii = generate_radii(num_clusters,min_radius,max_radius)
    error = random.uniform(0, max_error)
    points = []
    for center,radius in zip(centers,radii):
        points.extend(generate_points(num_points,center,radius,error))
    generate_csv(points,title)

def generate_csv(points, title):
    filename = f'src/experiments/data/{title}'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y'])
        writer.writerows(points)

def parse_experiment(title = 'experiment'):
    points = []
    filename = f'src/experiments/data/{title}'
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            points.append((float(row['x']), float(row['y'])))
    return points