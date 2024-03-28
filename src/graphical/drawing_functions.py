import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def point(x, y, color='ro'):
    return plt.plot(x, y, color)

def circle(center, radius, thickness=1, color='blue'):
    return Circle(center, radius, linewidth=thickness, edgecolor=color, fill=False)


def draw_points_and_circles(points=[], circles=[], spacesize=100, title='Points and Clusters'):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    for p in points:
        point(*p)
    for c in circles:
        ax.add_patch(circle(*c))
        point(*c[0],'kx')
    setup_plot(title,spacesize)


def setup_plot(title,spacesize):
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.xlim(0, spacesize)
    plt.ylim(0, spacesize)
    plt.title('Points and Clusters')
    plt.grid(True)
    plt.show()

