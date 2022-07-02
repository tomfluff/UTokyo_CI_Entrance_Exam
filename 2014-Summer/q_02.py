

import math

def compute_A_R0(d):
    area = math.pow((10//d)+1,2) # 11 := 10 - 0 + 1
    return area

def compute_A_R1(d):
    area = math.pi * math.pow((10//d)+1,2)
    return math.floor(area)

def points_relation(a, b):
    return (a/b)*0.25

def main():
    d = 1.0
    num1 = compute_A_R0(d)
    num2 = compute_A_R1(d)
    print(points_relation(num1, num2))

if __name__ == "__main__":
    main()
