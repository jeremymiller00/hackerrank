def jumpingOnClouds(c):
    """
    c: a binary list
    """
    # always jump two if possible, if not one
    jumps = 0
    pos = 0
    while pos < len(c):
        if pos <= (len(c)-3) and c[pos+2] == 0:
            pos += 2
        elif pos <= (len(c)-2) and c[pos+1] == 0:
            pos += 1
        elif pos == len(c) - 1:
            return jumps
        jumps += 1
    return jumps


print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))