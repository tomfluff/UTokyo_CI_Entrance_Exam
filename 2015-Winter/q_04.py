import math
import numpy as np

def f_rec(n):
    if n < 1:
        return 1
    
    return int((161*f_rec(n-1) + 2457) % math.pow(2,24))

def f_dyn(n):
    res_arr = np.full(fill_value=1,dtype='int32', shape=(n+1))
    
    for i in range(1,n+1):
        res_arr[i] = int((161*res_arr[i-1] + 2457) % math.pow(2,24))
    
    return res_arr[n]

def main():
    print(f_dyn(1000000))

if __name__ == "__main__":
    main()