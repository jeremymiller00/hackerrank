def birthday(s, d, m):
    '''
    s: list[int]
    d: int, proxy for sum
    m: int, proxy for window size

    return number of windows of size (m) that sum to (d)
    '''
    result = 0
    assert m <= len(s)
    for i in range(len(s) - m + 1):
        if sum(s[i:i+m]) == d:
            result += 1
    return result


