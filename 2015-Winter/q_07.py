import math
import numpy as np

def g_dyn(n, p=(1<<26)):
    last = 1
    a = 1103515245
    c = 12345
    for i in range(1,n+1):
        last = (a * last + c) & (p-1)
    
    return last

# The answer is obviously 2^26 because the 
def g_find_k_naive(n, p=(1<<26)):
    g_n = last = g_dyn(n, p)

    found = False
    a = 1103515245
    c = 12345
    i = 0
    while not found:
        i += 1
        last = (a * last + c) & (p-1)
        if g_n == last:
            found = True
    return i

def h_find_k(n):
    p = 1<<10
    return g_find_k_naive(n,p)

def main():
    n = 1
    k = h_find_k(n)
    print(f"n={n}, k={k}")

if __name__ == "__main__":
    main()