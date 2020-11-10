def abs(X):
    if X < 0:
        return X * -1
    else:
        return X

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):

    CatA = abs(z-x)
    CatB = abs(z-y)
    if CatA == CatB:
        return 'Mouse C'
    elif CatA < CatB:
        return 'Cat A'
    else:
        return 'Cat B'