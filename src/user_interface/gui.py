from experiments.experiment_results import draw_experiment_result, evaluate_new_points, parse_points
from user_interface import drawing_functions
from experiments import generate_experiment
from maths.best_fit_circle import best_fit_circle
from ring_clustering.algorithm import ring_clustering
from ring_clustering.init import Initialization
import tkinter as tk
from tkinter import ttk
import os


def generate_experiment_screen(root):
    def run_algorithm():
        num_points = int(points_entry.get())
        num_clusters = int(clusters_entry.get())
        max_error = float(max_error_entry.get())
        experiment_title = title_entry.get() + '.csv'

        # Generate experiment and obtain points
        generate_experiment.generate_exp(num_points, num_clusters, max_error=max_error, title=experiment_title)
        points = generate_experiment.parse_experiment(experiment_title)
        drawing_functions.draw_points_and_circles(points, title=experiment_title)


    # Experiment generation screen
    generate_exp_window = tk.Toplevel(root)
    generate_exp_window.title("Generate Experiment")

    # Experiment generation
    ttk.Label(generate_exp_window, text="Points per circular pattern:").grid(row=0, column=0)
    points_entry = ttk.Entry(generate_exp_window)
    points_entry.grid(row=0, column=1)

    ttk.Label(generate_exp_window, text="Number of circular patterns:").grid(row=1, column=0)
    clusters_entry = ttk.Entry(generate_exp_window)
    clusters_entry.grid(row=1, column=1)

    ttk.Label(generate_exp_window, text="Maximum uncertainty in circular patterns:").grid(row=2, column=0)
    max_error_entry = ttk.Entry(generate_exp_window)
    max_error_entry.grid(row=2, column=1)

    ttk.Label(generate_exp_window, text="Experiment Title:").grid(row=3, column=0)
    title_entry = ttk.Entry(generate_exp_window)
    title_entry.grid(row=3, column=1)

    # Execution button
    ttk.Button(generate_exp_window, text="Generate Experiment", command=run_algorithm).grid(row=9, columnspan=2)

def run_algorithm(root):
    def run_algorithm():
        experiment_title = title_combobox.get()
        selected_initialization = initialization_combobox.get()
        initialization = Initialization[selected_initialization]
        max_iterations = int(max_iterations_entry.get())
        min_convergence = 0.5
        allowed_error = float(allowed_error_entry.get())
        allowed_cluster_equivalence_rate = float(allowed_cluster_equivalence_rate_entry.get())
        k = int(k_entry.get())

        points = generate_experiment.parse_experiment(experiment_title)

        ring_clustering(
            points,
            k,
            title=experiment_title,
            initialization=initialization,
            min_convergence=min_convergence,
            max_iterations=max_iterations,
            allowed_error=allowed_error,
            allowed_cluster_equivalence_rate=allowed_cluster_equivalence_rate
        )

    # Algorithm setup screen
    algorithm_window = tk.Toplevel(root)
    algorithm_window.title("Ring Like Clustering")

    # Algorithm setup
    ttk.Label(algorithm_window, text="Experiment:").grid(row=0, column=0)
    experiment_files = [file for file in os.listdir("src/experiments/data") if file.endswith('.csv')]
    title_combobox = ttk.Combobox(algorithm_window, values=experiment_files)
    title_combobox.grid(row=0, column=1)

    ttk.Label(algorithm_window, text="K:").grid(row=1, column=0)
    k_entry = ttk.Entry(algorithm_window)
    k_entry.grid(row=1, column=1)

    ttk.Label(algorithm_window, text="Initialization:").grid(row=2, column=0)
    initialization_combobox = ttk.Combobox(algorithm_window, values=[init.name for init in Initialization])
    initialization_combobox.grid(row=2, column=1)

    ttk.Label(algorithm_window, text="Maximum number of iterations:").grid(row=3, column=0)
    max_iterations_entry = ttk.Entry(algorithm_window)
    max_iterations_entry.grid(row=3, column=1)

    ttk.Label(algorithm_window, text="Allowed noise:").grid(row=4, column=0)
    allowed_error_entry = ttk.Entry(algorithm_window)
    allowed_error_entry.grid(row=4, column=1)

    ttk.Label(algorithm_window, text="Maximum cluster equivalence rate:").grid(row=5, column=0)
    allowed_cluster_equivalence_rate_entry = ttk.Entry(algorithm_window)
    allowed_cluster_equivalence_rate_entry.grid(row=5, column=1)

    # Execution button
    ttk.Button(algorithm_window, text="Execute Algorithm", command=run_algorithm).grid(row=6, columnspan=2)

def revisit_experiment_screen(root):
    def revisit_experiment():
        experiment_results = results_combobox.get()
        draw_experiment_result(experiment_results)

    results_window = tk.Toplevel(root)
    results_window.title("Results Screen")

    ttk.Label(results_window, text="Experiment Results:").grid(row=0, column=0)
    experiment_files = [file for file in os.listdir("src/experiments/data/results") if file.endswith('.csv')]
    results_combobox = ttk.Combobox(results_window, values=experiment_files,  width=80)
    results_combobox.grid(row=0, column=1)

    ttk.Button(results_window, text="Results", command=revisit_experiment).grid(row=1, columnspan=2)

def evaluate_points_screen(root):
    def evaluate_points():
        experiment_results = results_combobox.get()
        evaluate_new_points(parse_points(points_entry),experiment_results)

    evaluate_window = tk.Toplevel(root)
    evaluate_window.title("Evaluate Screen")

    ttk.Label(evaluate_window, text="Experiment Results:").grid(row=0, column=0)
    experiment_files = [file for file in os.listdir("src/experiments/data/results") if file.endswith('.csv')]
    results_combobox = ttk.Combobox(evaluate_window, values=experiment_files,  width=80)
    results_combobox.grid(row=0, column=1)

    ttk.Label(evaluate_window, text="Points [(x1,y1), (x2,y2), ...]:").grid(row=1, column=0)
    points_entry = ttk.Entry(evaluate_window, width=50)
    points_entry.grid(row=1, column=1)

    ttk.Button(evaluate_window, text="Results", command=evaluate_points).grid(row=2, columnspan=2)

