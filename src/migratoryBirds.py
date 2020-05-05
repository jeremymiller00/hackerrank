def migratoryBirds(arr):
    '''
    Return most frequent integer in array
    If tie, return min
    '''
    counter = {}
    key_set = set(arr)
    for k in key_set:
        counter[k] = arr.count(k)
    candidates = [k for k in counter.keys() if counter[k] == max(counter.values())]
    return min(candidates)
