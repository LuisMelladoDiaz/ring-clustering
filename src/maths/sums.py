def summation(X):
    return sum(X)

def summation_squares(X):
    return sum(x**2 for x in X)

def summation_productXY(X,Y):
    return sum(x * y for x, y in zip(X, Y))

def summation_addition_of_sqaresXY(X,Y):
    return sum(x**2 + y**2 for x, y in zip(X, Y))

def summation_productX_addition_of_sqaresXY(X,Y):
    return sum(x*(x**2 + y**2) for x, y in zip(X, Y))
