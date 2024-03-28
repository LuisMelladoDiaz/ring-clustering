from graphical import drawing_functions
from experimental_data import generate_experiment
from ring_clustering.algorithm import ring_clustering
from ring_clustering.init import Initialization

def main():
    #generate_experiment.generate_exp(40,3,max_error=0,title='Ideal_Experiment')
    points = generate_experiment.parse_experiment('Ideal_Experiment')
    #drawing_functions.draw_points_and_circles(points, title='Ideal Experiment')

    ring_clustering(points,3,initialization=Initialization.RANDOM,max_iterations=1)


if __name__ == "__main__":
    main()

