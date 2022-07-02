
import math


def get_area_of_Kn(side,k,i):
    if i > k:
        return 0
    height = math.sqrt(3)*side/2
    area = side*height/2

    return area + 2 * get_area_of_Kn(side/3,k,i+1)

# x,y q,z := sqrt((|q-x|)^2+(|z-y|)^2)
# height := sqrt(3)*side / 2 // sqrt(side^2 - (side/2)^2)
# area of equi triangle := side * height / 2

def get_area_of_Kn_main(triangle, k):
    p1,p2 = triangle[0], triangle[1]
    side = math.sqrt(math.pow(p1[0]-p2[0],2) + math.pow(p1[1]-p2[1],2))
    height = math.sqrt(3)*side/2

    return side*height/2 + 3 * get_area_of_Kn(side/3,k,1)
    

def compute_A_Kn(area,d):
    return area

def compute_A_kn_d(k,d):
    s = 10
    starting_triangle = [(0,0), (0,(s//d)), (((s//d))/2,(((s//d))/2)*math.sqrt(3))]
    print(starting_triangle)
    area = get_area_of_Kn_main(starting_triangle,k)

    return math.floor(compute_A_Kn(area,d))

def main():
    k = 0
    d = 1
    print(compute_A_kn_d(k,d))

if __name__ == "__main__":
    main()