from graphical import drawing_functions
from experimental_data import generate_experiment
from ring_clustering.algorithm import ring_clustering
from ring_clustering.init import Initialization

def main():
    #generate_experiment.generate_exp(3,3,max_error=0,title='Low_Point_Number')
    points = generate_experiment.parse_experiment('Ideal_Experiment')

    ring_clustering(points,3,initialization=Initialization.RANDOM,max_iterations=1)


if __name__ == "__main__":
    main()

