# def repeatedString(s, n):
#     full_string = ""
#     while len(full_string) <= n:
#         full_string += s
#     concat_string = full_string[:n]
#     return concat_string.count('a')

def repeatedString(s, n):
    one_pass = s.count('a')
    # find the number of full passes
    full_passes = n // len(s)
    rem_len = n % len(s)
    # store remainder
    # find the substring count in 
    rem_count = s[:rem_len].count('a')
    out = (full_passes * one_pass) + rem_count
    return out

print(repeatedString("aba", 10))