def flip_arr(a, i):
    """
    a: array
    d: new first index
    """
    f = a[i:]
    r = a[:i]
    f.extend(r)
    return f

def rotLeft(a, d):
    """
    a: array to be rotated
    d: number of left rotations
    """
    if len(a) == d:
        return a
    elif len(a) > d:
        return flip_arr(a,d)
    else:
        new_start = len(a) - (len(a) % d)
        return flip_arr(a, new_start)

# print(rotLeft([1, 2, 3, 4, 5], 4))
print(flip_arr([1, 2, 3, 4, 5], 3))