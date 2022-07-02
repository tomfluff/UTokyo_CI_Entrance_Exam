import math
import numpy as np

def g_dyn(n):
    last = 1
    p = int(math.pow(2, 26))
    a = 1103515245
    c = 12345
    for i in range(1,n+1):
        if i + 5 > n+1:
            print(f"i={i}, last={last}, next={(a * last + c) & (p-1)}")
        last = (a * last + c) & (p-1)
    
    return last

# The answer is obviously 2^26 because the 
def g_find_k_naive(n):
    g_n = last = g_dyn(n)

    found = False
    p = int(math.pow(2, 26))
    a = 1103515245
    c = 12345
    i = 0
    while not found:
        i += 1
        last = (a * last + c) & (p-1)
        if g_n == last:
            found = True
    return i


def g_find_k_math():
    return 1 << 26


def main():
    n = 100
    k = g_find_k_math()
    print(f"n={n}, k={g_find_k_naive(n)}, n(mod)={g_dyn(n)}, n+k(mod)={g_dyn(n+k)}")

if __name__ == "__main__":
    main()