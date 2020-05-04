from functools import reduce

def getTotalX(a, b):

    def gcd(a, b):
        while a % b != 0:
            a, b = b, (a % b)
        return b
    
    def lcm(a, b):
        return a * b // gcd(a, b)

    min_gcd = reduce(gcd, b)
    max_lcm = reduce(lcm, a)
    count = sum([1 for x in range(max_lcm, min_gcd+1, max_lcm) if min_gcd % x == 0])
 
    return count