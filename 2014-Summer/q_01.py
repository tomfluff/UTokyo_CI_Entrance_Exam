import math

def compute_A_R0(d):
    side = (10 / d) + 1
    area = side * side
    return math.floor(area)

def main():
    d = 0.5
    num = compute_A_R0(d)
    print(num)

if __name__ == "__main__":
    main()
