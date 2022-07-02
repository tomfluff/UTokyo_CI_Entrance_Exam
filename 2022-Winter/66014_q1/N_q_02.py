from locale import atoi
import numpy as np

# N rows, M colums
M = N = 30

def check_size_constraint(a, b):
    assert len(a) == len(b)
    if a[0] >= b[0] or a[0] < 0 or a[1] >= b[1] or a[1] < 0:
        return False

def read_board_from_file(fname):
    b = np.full((N,M), 0)
    with open(fname, 'r') as f:
        for l in f.readlines():
            ps = l.split(':')
            for p in ps:
                n_s = p.split(',')
                b[atoi(n_s[0]),atoi(n_s[1])] = 1
    return b

def check_condition_on_board(b, p, con=(1,1), sym=0):
    for k in range(max(M,N)):
        n_p = (p[0]+(k*con[0]), p[1]+(k*con[1]))
        if check_size_constraint(n_p,b.shape) == False:
            return True
        if b[n_p[0],n_p[1]] != sym:
            return False
    return True

def check_full_direction(b, p, con=(1,1), sym=0):
    return check_condition_on_board(b, p, con, sym) and check_condition_on_board(b, p, (-1*con[0],-1*con[1]), sym=0)

def check_rule_for_point(b, p):
    rule_a = True
    i,j = p
    # col
    rule_a &= check_full_direction(b,(i,j),con=(1,0),sym=0)
    # row
    rule_a &= check_full_direction(b,(i,j),con=(0,1),sym=0)
    # major diag
    rule_a &= check_full_direction(b,(i,j),con=(-1,1),sym=0)
    # minor diag
    rule_a &= check_full_direction(b,(i,j),con=(1,1),sym=0)
    return rule_a

def main():
    b = read_board_from_file('2022-Winter/data2.txt')
    assert(b[22,7] == 1 and b[8,14] == 1 and b[20,11] == 1)
    for i in range(28,N):
        for j in range(M):
            if check_rule_for_point(b, (i,j)):
                print(f"Q2=({i},{j})")

    print(b)


if __name__ == "__main__":
    main()
