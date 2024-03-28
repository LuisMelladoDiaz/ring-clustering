from sympy import symbols, Eq, solve
from sums import *
import math

def best_fit_circle(points):
    n = len(points)
    X,Y = extract_coordinates(points)
    A,B,C = solve_system(X,Y,n)
    h,k = compute_center(A,B,C)
    radius = compute_radius(A,B,C)
    cluster = ((h,k),radius)
    return cluster


def solve_system(X,Y,n):
    A, B, C = symbols('A','B','C')

    eq1 = Eq(summation_squares(X)*A
        + summation_productXY(X,Y)*B
        + summation(X)*C,
    summation_productX_addition_of_sqaresXY(X,Y))

    eq2 = Eq(summation_squares(Y)*B
        + summation_productXY(X,Y)*A
        + summation(Y)*C,
    summation_productX_addition_of_sqaresXY(Y,X))

    eq3 = Eq(summation(X)*A
        + summation(Y)
        + n,
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
    for x,y,color in points:
        X.append(x)
        Y.append(y)
    return X,Y
