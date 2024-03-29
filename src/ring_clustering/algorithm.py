from asyncio.windows_events import NULL
from maths.best_fit_circle import best_fit_circle
from ring_clustering.halting import check_halting
from ring_clustering.init import Initialization, init_clusters
from graphical import drawing_functions
from utils.cluster_generation import build_clusters
from maths.distances import compute_membership


def ring_clustering(points, num_clusters, initialization=Initialization.RANDOM, centers_color = 'kx', max_iterations = 10, min_convergence = NULL):

    #INITIALIZATION
    centers, radii = init_clusters(num_clusters, initialization, centers_color)
    clusters = build_clusters(centers,radii)
    halt = False
    num_iterations = 0
    convergence = 100

    drawing_functions.draw_points_and_circles(points, clusters, title='Problem')
    membership, classification, points, clusters = compute_membership(clusters, points)
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
        membership, classification, points, clusters = compute_membership(clusters, points)
        #DRAW RESULT
        drawing_functions.draw_points_and_circles(points, clusters, title=('Iteration',num_iterations))

    print('Algorith halted after', num_iterations, 'iteration/s with convergence of', convergence)
    print('Centers', centers)
