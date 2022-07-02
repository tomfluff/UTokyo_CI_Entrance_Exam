
import numpy as np

def get_sum_of_dec(a,b):
    if len(a) >= len(b):
        a_rev = a[::-1]
        b_rev = b[::-1]
    else:
        a_rev = b[::-1]
        b_rev = a[::-1]
    res = ""
    
    i = 0
    c = 0
    for d in a_rev:
        if i >= len(b_rev):
            b_n = 0
        else:
            b_n = int(b_rev[i])
        r = int(d) + b_n + c
        if r > 9:
            r = r % 10
            c = 1
        else:
            c = 0
        res += str(r)
        i += 1
    
    if c != 0:
        res += str(c)

    return res[::-1]

def f_dyn(x):
    mem = ['0' for i in range(x)]
    mem[0] = '1'
    if x > 1:
        mem[1] = '1'
    for i in range(3,x+1):
        r = get_sum_of_dec(mem[i-2], mem[i-3])
        mem[i-1] = r
    
    return mem[x-1]

def main():
    ans = f_dyn(140)
    print(ans)

if __name__ == "__main__":
    main()