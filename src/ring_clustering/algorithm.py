from asyncio.windows_events import NULL
import random
from experiments.experiment_results import save_results
from maths.best_fit_circle import best_fit_circle
from ring_clustering.halting import check_halting
from ring_clustering.init import Initialization, init_clusters
from user_interface import drawing_functions
from ring_clustering.post_processing import remove_equivalent_clusters, remove_noise
from utils.cluster_generation import build_clusters
from maths.distances import compute_membership


def ring_clustering(points, num_clusters, initialization=Initialization.RANDOM, centers_color = 'kx', max_iterations = 10, min_convergence = NULL, allowed_error = NULL, allowed_cluster_equivalence_rate=NULL, title='Experiment'):

    #INITIALIZATION
    centers, radii = init_clusters(num_clusters, initialization, centers_color, points)
    initial_clusters = build_clusters(centers,radii)
    clusters = initial_clusters
    halt = False
    num_iterations = 0
    convergence = 100

    drawing_functions.draw_points_and_circles(points, clusters, title='Problem')
    membership, classification, points, clusters, error = compute_membership(clusters, points)
    drawing_functions.draw_points_and_circles(points, clusters, title='Initial classes')

    #MAIN LOOP
    while (halt == False):
        num_iterations +=1
        halt = check_halting(num_iterations,convergence,max_iterations,min_convergence)
        convergence = 100 #Compute convergence here
        new_clusters = []
        for cluster, pts in classification.items():
            new_clusters.append(best_fit_circle(pts))
        clusters = new_clusters
        membership, classification, points, clusters, error = compute_membership(clusters, points)
        #DRAW RESULT
        drawing_functions.draw_points_and_circles(points, clusters, title=('Iteration',num_iterations))

    #DRAW RESULT
    clusters = remove_equivalent_clusters(clusters, allowed_cluster_equivalence_rate)
    membership, classification, points, clusters, error = compute_membership(clusters, points)
    points = remove_noise(points,error,allowed_error)
    drawing_functions.draw_points_and_circles(points, clusters, title='Noise removed')

    print('Algorith halted after', num_iterations, 'iteration/s with convergence of', convergence)
    print('Centers', centers)

    #SAVE RESULT
    experiment_id = random.randint(1, 1000)
    experiment_results_title = f'{title}_{num_clusters}Clusters_{initialization}_PostProcessing{allowed_error}&{allowed_cluster_equivalence_rate}_{experiment_id}'
    save_results(points, initial_clusters, clusters, experiment_results_title)
