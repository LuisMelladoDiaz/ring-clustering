from user_interface import gui
import tkinter as tk
from tkinter import ttk

def main():
    def open_generate_experiment():
        gui.generate_experiment_screen(root)
    def open_run_algorithm():
        gui.run_algorithm(root)
    def open_revisit_experiment():
        gui.revisit_experiment_screen(root)
    def open_evaluate_points():
        gui.evaluate_points_screen(root)

    # Create main screen
    root = tk.Tk()
    root.title("Ring-Like Clustering GUI")

    ttk.Button(root, text="Generate Experiment", command=open_generate_experiment).pack()
    ttk.Button(root, text="Run Algorithm Over Experiment", command=open_run_algorithm).pack()
    ttk.Button(root, text="Revisit Experiment Result", command=open_revisit_experiment).pack()
    ttk.Button(root, text="Evaluate New Points", command=open_evaluate_points).pack()

    root.mainloop()

if __name__ == "__main__":
    main()


