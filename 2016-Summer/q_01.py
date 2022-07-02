'''
123 = 27
3*4^0+2*4^1+1*4^2=27
3+8+16=27
'''
import math


def quat_to_dec(n) -> int:
    p = 0
    base = 4
    res = 0

    while n != 0:
        c = n % 10
        assert c < 4
        res += c*math.pow(base,p)
        p += 1
        n = n // 10
    
    return int(res)

def main():
    n = 321
    print(quat_to_dec(n))

if __name__ == "__main__":
    main()
