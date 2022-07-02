
import numpy as np

def f(x):
    assert(x>=0)
    if x <= 2:
        return 1
    return f(x-1)+f(x-2)

def f_dyn(x):
    mem = np.array([0 for i in range(x)], dtype='int64')
    mem[0] = 1
    if x > 1:
        mem[1] = 1
    for i in range(3,x+1):
        mem[i-1] = mem[i-2] + mem[i-3]
    
    return mem[x-1]

def main():
    ans = f_dyn(50)
    print(ans)

if __name__ == "__main__":
    main()