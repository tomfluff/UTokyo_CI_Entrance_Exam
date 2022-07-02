from locale import atoi
import numpy as np

N = 20
M = 20

def count_sym(b, sym):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if b[i,j] == sym:
                cnt += 1
    return cnt
            

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

def check_black_down_right(b,i,j):
    max_k = -1
    for k in range(1,min(N,M)):
        if i+k >= N or j+k >= M:
            return max_k
        if b[i+k,j+k] == 0:
            return max_k
        if b[i+k,j+k] == 2:
            max_k = k

def check_black_up_right(b,i,j):
    max_k = -1
    for k in range(1,min(N,M)):
        if i-k < 0 or j+k >= M:
            return max_k
        if b[i-k,j+k] == 0:
            return max_k
        if b[i-k,j+k] == 2:
            max_k = k

def check_black_down_left(b,i,j):
    max_k = -1
    for k in range(1,min(N,M)):
        if i+k >= N or j-k < 0:
            return max_k
        if b[i+k,j-k] == 0:
            return max_k
        if b[i+k,j-k] == 2:
            max_k = k
            
def check_black_up_left(b,i,j):
    max_k = -1
    for k in range(1,min(N,M)):
        if i-k < 0 or j-k < 0:
            return max_k
        if b[i-k,j-k] == 0:
            return max_k
        if b[i-k,j-k] == 2:
            max_k = k

def check_black_right(b,i,j):
    max_k = -1
    for k in range(1,M):
        if j+k >= M:
            return max_k
        if b[i,j+k] == 0:
            return max_k
        if b[i,j+k] == 2:
            max_k = k

def check_black_left(b,i,j):
    max_k = -1
    for k in range(1,M):
        if j-k < 0:
            return max_k
        if b[i,j-k] == 0:
            return max_k
        if b[i,j-k] == 2:
            max_k = k

def check_black_down(b,i,j):
    max_k = -1
    for k in range(1,N):
        if i+k >= N:
            return max_k
        if b[i+k,j] == 0:
            return max_k
        if b[i+k,j] == 2:
            max_k = k

def check_black_up(b,i,j):
    max_k = -1
    for k in range(1,N):
        if j-k < 0:
            return max_k
        if b[i-k,j] == 0:
            return max_k
        if b[i-k,j] == 2:
            max_k = k

def main():
    b = np.full((N,M),0)
    b,gray_c = mark_sym_in_board(b,'gray.txt',1)
    b,black_c = mark_sym_in_board(b,'black.txt',2)
    i = 5
    j = 6
    # This is a mistake:
    # b = b.transpose() 
    # ----
    b[i,j] = 2
    k = check_black_down(b,i,j)
    
    if k > 0:
        for l in range(k):
            b[i+l,j] = 2
    k = check_black_up(b,i,j)
    
    if k > 0:
        for l in range(k):
            b[i-l,j] = 2

    k = check_black_left(b,i,j)
    
    if k > 0:
        for l in range(k):
            b[i,j-l] = 2
    k = check_black_right(b,i,j)
    
    if k > 0:
        for l in range(k):
            b[i,j+l] = 2

    k = check_black_up_left(b,i,j)
    
    if k > 0:
        for l in range(k):
            b[i-l,j-l] = 2
    k = check_black_up_right(b,i,j)
    
    if k > 0:
        for l in range(k):
            b[i-l,j+l] = 2
    
    k = check_black_down_left(b,i,j)
    
    if k > 0:
        for l in range(k):
            b[i+l,j-l] = 2
    k = check_black_down_right(b,i,j)
    
    if k > 0:
        for l in range(k):
            b[i+l,j+l] = 2
    gray_c = count_sym(b, 1)
    black_c = count_sym(b, 2)

    print(f"black: {black_c}")
    print(f"gray: {gray_c}")

if __name__ == "__main__":
    main()