import math

def f_rec(n):
    if n < 1:
        return 1
    
    return int((161*f_rec(n-1) + 2457) % math.pow(2,24))
    

def main():
    print(f_rec(100))

if __name__ == "__main__":
    main()