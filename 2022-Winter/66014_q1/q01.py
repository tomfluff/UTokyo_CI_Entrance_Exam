from locale import atoi
import numpy as np

def main():
    lines = []
    inter = []
    max_r = 44
    max_c = 44
    with open('data1.txt', 'r') as f:
        lines = f.readlines()
    
    for l in lines:
        pos = l.split(':')
        for p in pos:
            r,c = p.split(',')
            inter.append((atoi(r),atoi(c)))
            if inter[-1][0] > max_r:
                max_r = r
            if inter[-1][1] > max_c:
                max_c = c
    
    # Mistake
    b = np.full((max_c+1,max_r+1), 0)
    for r,c in inter:
        b[c,r] = 1
    # -----
    
    for i in range(max_c+1):
        b_a = [b[k,i+k] for k in range(max_c-i+1)]
        b_b = [b[k,i-k] for k in range(i+1)]
        b_c = [b[k,i] for k in range(max_r+1)]

        if np.sum(b_a) == 0 and np.sum(b_b) == 0 and np.sum(b_c) == 0:
            print(f"(0,{i})")


if __name__ == "__main__":
    main()