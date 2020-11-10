from functools import reduce

def transpose(m):
    out = []
    for j in range(len(m[0])):
        row = []
        for i in range(len(m)):
            row.append(m[i][j])
        out.append(row)
    return out


def is_magic_square(m):
    row_sums = [reduce(lambda x,y: x+y, m[i]) for i in range(len(m))]
    col_sums = [reduce(lambda x,y: x+y, transpose(m)[i]) for i in range(len(m))]
    d1 = 0
    d2 = 0
    for i in range(len(m)):
        d1 += m[i][i]
        d2 += m[i][2-i]
    diag_sums =[d1, d2]
    num_set = set([val for row in m for val in row])

    if sum(row_sums) == sum(col_sums) == sum(diag_sums)*1.5:
        if len(num_set) == 9:
            return True
    return False

if __name__ == '__main__':
    m = [[5,3,4], [1,5,8], [6,4,2]]
    # print(transpose(m))
    print(is_magic_square(m))