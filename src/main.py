from graphical import drawing_functions
import matplotlib.pyplot as plt

def main():
    points = [(20, 30), (50, 70), (80, 10)]
    circles = [((40, 40), 15, 2, 'red'), ((70, 50), 20, 1, 'green'), ((30, 50), 30, 1)]
    drawing_functions.draw_points_and_circles(points,circles)


if __name__ == "__main__":
    main()

