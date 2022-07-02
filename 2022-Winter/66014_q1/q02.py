import numpy as np
from locale import atoi

def get_black_place_for_line(b,l):
    max_c = b.shape[0]-1
    max_r = b.shape[1]-1
    print(max_c,max_r)
    for i in range(max_c+1):
        b_a = [b[i+k,l+k] for k in range(min(max_c-i,max_r-l)+1)]
        b_b = [b[i-k,l+k] for k in range(min(i,max_r-l)+1)]
        b_c = [b[i,k] for k in range(max_r+1)]
        b_d = [b[i-k,l-k] for k in range(min(l,i)+1)]
        b_e = [b[i+k,l-k] for k in range(min(l,max_c-i)+1)]

    if np.sum(b_a) == 0 and np.sum(b_b) == 0 and np.sum(b_c) == 0 and np.sum(b_d) ==0 and np.sum(b_e) == 0:
        print(f"(0,{i})")

def main():
    lines = []
    inter = []
    max_r = 3#29
    max_c = 4#29
    with open('t.txt', 'r') as f:
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
    
    b = np.full((max_c+1,max_r+1), 0)
    for r,c in inter:
        b[c,r] = 1
    
    print(b, b.shape)
    print(b[2,0])
    get_black_place_for_line(b,3)
    #print(b[29])
    
    #get_black_place_for_line(b,28)
    #get_black_place_for_line(b,29)

if __name__ == "__main__":
    main()