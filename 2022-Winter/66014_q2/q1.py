from locale import atoi
import numpy as np

N = 20
M = 20

def mark_sym_in_board(b,fname,sym):
    cnt = 0
    with open(fname,'r') as f:
        for l in f.readlines():
            pcs = l.split(':')
            cnt += len(pcs)
            for pp in pcs:
                p = pp.split(',')
                i = atoi(p[0])
                j = atoi(p[1])
                assert(b[i,j] == 0)
                b[i,j] = sym
    return b,cnt

def main():
    b = np.full((N,M),0)
    b,gray_c = mark_sym_in_board(b,'gray.txt',1)
    b,black_c = mark_sym_in_board(b,'black.txt',2)
    print(f"black: {black_c}")
    print(f"gray: {gray_c}")

if __name__ == "__main__":
    main()