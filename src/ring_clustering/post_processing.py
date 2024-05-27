from asyncio.windows_events import NULL
from turtle import distance

from maths.distances import distance_point_point

def remove_noise(points, error, allowed_error):
    noiseless_points = []
    if allowed_error != NULL:
        for p in points:
            x,y,*_ = p
            if (error[(x,y)] <= allowed_error):
                noiseless_points.append(p)
    return noiseless_points

def remove_equivalent_clusters(clusters, allowed_cluster_equivalence_rate):
    unequivalent_clusters = clusters
    if allowed_cluster_equivalence_rate != NULL:
        # FOR EACH CLUSTER PAIR
        for clusterA in clusters:
            centerA, radiusA, *_ = clusterA
            for clusterB in clusters:
                if clusterB != clusterA:
                    centerB, radiusB, *_ = clusterB
                    radius_equivalence_rate = 1 - (abs(radiusA-radiusB))/100
                    center_equivalence_rate = 1 - distance_point_point(centerA,centerB)/100
                    equivalence_rate = (radius_equivalence_rate + center_equivalence_rate)/2
                    # IF THEY ARE TOO SIMILAR REMOVE THEM
                    if equivalence_rate > allowed_cluster_equivalence_rate:
                        unequivalent_clusters.remove(clusterB)
    return unequivalent_clusters





