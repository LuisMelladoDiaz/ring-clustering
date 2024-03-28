import random

def points_coloring(points, membership):
    colored_points = []
    print (membership)
    for p in points:
        x,y = p
        color = COLORS[membership[p][0] % 7]
        print(color)
        colored_points.append((x,y,color))

    return colored_points

def cluster_coloring(clusters):
    colored_clusters = []
    for i,c in enumerate(clusters):
        print(c)
        center,radius = c
        color = COLORS_RGB_NORMALIZED[i % 7]
        colored_clusters.append((center,radius,color))

    return colored_clusters

COLORS = ['ro','go','bo','ko','co','mo','yo']
COLORS_RGB = [
    (255, 0, 0),    # 'ro' - Rojo
    (0, 128, 0),    # 'go' - Verde
    (0, 0, 255),    # 'bo' - Azul
    (0, 0, 0),      # 'ko' - Negro
    (0, 255, 255),  # 'co' - Cian
    (255, 0, 255),  # 'mo' - Magenta
    (255, 255, 0)   # 'yo' - Amarillo
]
COLORS_RGB_NORMALIZED = [(r / 255, g / 255, b / 255) for r, g, b in COLORS_RGB]
