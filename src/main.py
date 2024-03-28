from graphical import drawing_functions
from experimental_data import generate_experiment

def main():
    generate_experiment.generate_exp(50,3)
    points = generate_experiment.parse_experiment()
    drawing_functions.draw_points_and_circles(points)


if __name__ == "__main__":
    main()

