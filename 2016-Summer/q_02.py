'''
bcd = 83
3*8^0+2*8^1+1*8^2 = 3+16+64 = 83
'''
import math

def oct_to_dec(n) -> int:
    base = 8
    p = 0
    res = 0
    while n != '':
        c = ord(n[-1]) - 97
        assert c < 8
        res += c*math.pow(base,p)
        p += 1
        n = n[:-1]
    return int(res)

def main():
    n = "bcd"
    print(oct_to_dec(n))

if __name__ == "__main__":
    main()
