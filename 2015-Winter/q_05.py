import math
import numpy as np


def g_dyn(n):
    last = 1
    p = int(math.pow(2, 26))
    a = 1103515245
    c = 12345
    for i in range(1,n+1):
        last = (a * last + c) & (p-1)
    
    return last

def main():
    print(f"g(2)={g_dyn(2)}, g(3)={g_dyn(3)}")

if __name__ == "__main__":
    main()