from graphical import drawing_functions
from experimental_data import generate_experiment
from maths.best_fit_circle import best_fit_circle
from ring_clustering.algorithm import ring_clustering
from ring_clustering.init import Initialization

def main():
    generate_experiment.generate_exp(30,3,max_error=0.1,title='Experiment')
    points = generate_experiment.parse_experiment('Experiment')

    ring_clustering(points,3,initialization=Initialization.RANDOM,max_iterations=1,allowed_error=3,allowed_cluster_equivalence_rate=0.85)


if __name__ == "__main__":
    main()

