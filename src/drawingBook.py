import math

def pageCount(n, p):
    f_turns = 0
    if p == 1 or p == n:
        return 0
    current_page_f = 1
    while current_page_f <= p:
        current_page_f += 2
        f_turns += 1
    b_turns = 0
    if n % 2 == 0:
        current_page_b = n
    else:
        current_page_b = n + 1
    while current_page_b >= p:
        current_page_b -= 2
        b_turns += 1
    return min(f_turns, b_turns)
