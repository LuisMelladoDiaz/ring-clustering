from random import randint
from sympy import symbols, Eq, solve
import math
from maths.distances import distance_point_circle, distance_point_point

from maths.sums import *

def best_fit_circle(points):
    n = len(points)
    X,Y = extract_coordinates(points)
    A,B,C = solve_system(X,Y,n)
    h,k = compute_center(A,B)
    radius = compute_radius(A,B,C)
    cluster = ((h,k),radius)
    return cluster

def best_fit_circle_weighted(points, cluster_points, cluster):
    X,Y = extract_coordinates(points)
    weighted_points = weight_points(list(zip(X, Y)), cluster_points, cluster)
    return best_fit_circle(weighted_points)


def solve_system(X,Y,n):
    A, B, C = symbols('A B C')

    eq1 = Eq(summation_squares(X)*A
        + summation_productXY(X,Y)*B
        + summation(X)*C,
    summation_productX_addition_of_sqaresXY(X,Y))

    eq2 = Eq(summation_squares(Y)*B
        + summation_productXY(X,Y)*A
        + summation(Y)*C,
    summation_productX_addition_of_sqaresXY(Y,X))

    eq3 = Eq(summation(X)*A
        + summation(Y)*B
        + n*C,
    summation_addition_of_sqaresXY(X,Y))

    sol = solve((eq1, eq2, eq3), (A, B, C))
    return sol[A],sol[B],sol[C]

def compute_center(A,B):
    return A/2, B/2

def compute_radius(A,B,C):
    radius = (math.sqrt(4*C + A**2 + B**2))/2
    return radius

def extract_coordinates(points):
    X = []
    Y = []
    for x,y,*_ in points:
        X.append(x)
        Y.append(y)
    return X,Y

import random
import math

def weight_points(points, cluster_points, cluster):
    weighted_points = []
    max_distance = math.sqrt(100 * 100 + 100 * 100)
    for p in points:
        if p in cluster_points:
            if random.random() <= 0.8:
                weighted_points.append(p)
        else:
            distance = distance_point_circle(p, cluster)
            normalized_distance = distance / max_distance
            probability = math.exp(-5 * normalized_distance)
            random_value = randint(75,100)/100
            if random_value < probability:
                weighted_points.append(p)
    return weighted_points
