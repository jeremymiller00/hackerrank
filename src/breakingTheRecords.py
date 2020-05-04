def breakingRecords(scores):
    '''
    input: list[int]
    output: list[int]
    '''
    min_delta = 0
    max_delta = 0
    min = scores[0]
    max = scores[0]
    for item in scores[1:]:
        if item < min:
            min_delta += 1
            min = item
        if item > max:
            max_delta += 1
            max = item
    return [max_delta, min_delta]