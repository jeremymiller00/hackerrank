def divisibleSumPairs(n, k, ar):
    '''
    Print the number of ar[i],ar[j] pairs where i<j 
    and ar[i]+ar[j] is evenly divisible by k
    '''
    result = 0
    for i in range(len(ar)-1):
        for j in range(i+1, len(ar)):
            if (ar[i]+ar[j]) % k == 0:
                result += 1
    return result