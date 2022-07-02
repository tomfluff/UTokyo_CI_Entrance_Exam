import math

def f_rec(n):
    if n < 1:
        return 1
    
    return int((161*f_rec(n-1) + 2457) % math.pow(2,24))

def count_i():
    # assuming i starts from 1 to 100

    cnt = 0
    for i in range(1,100):
        r = f_rec(i)
        if r % 2 == 0:
            cnt += 1
    
    return cnt

def main():
    print(count_i())

if __name__ == "__main__":
    main()