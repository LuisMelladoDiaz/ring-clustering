from experimental_data.experiment_results import draw_experiment_result, evaluate_new_points
from graphical import drawing_functions
from experimental_data import generate_experiment
from maths.best_fit_circle import best_fit_circle
from ring_clustering.algorithm import ring_clustering
from ring_clustering.init import Initialization

def main():
    experiment_title = 'Experiment'
    generate_experiment.generate_exp(30,3,max_error=0.1,title=experiment_title)
    points = generate_experiment.parse_experiment(experiment_title)

    ring_clustering(points,3,initialization=Initialization.RANDOM,max_iterations=1,allowed_error=3,allowed_cluster_equivalence_rate=0.90)

    #results = 'Experiment_3Clusters_Initialization.RANDOM_PostProcessing3&0.9_295'
    #draw_experiment_result(results)
    #evaluate_new_points([(50,50), (70,25)],results)

if __name__ == "__main__":
    main()

