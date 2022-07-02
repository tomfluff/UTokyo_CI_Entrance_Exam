
from locale import atoi

WHITE = (255,255,255)

def main():
    lines = []
    pxls = []
    k = 4
    with open('2019-Summer/image2.txt', 'r') as f:
        lines = f.readlines()
    
    # Assume file is a one-line file
    for l in lines:
        ns = [atoi(x) for x in l.strip().split(' ')]
        for i in range(0,len(ns),3):
            pxls.append((ns[i],ns[i+1],ns[i+2],i//3))
            
    pxls_sr = sorted(pxls, key=lambda x: x[3], reverse=True)
    pxls_sr = sorted(pxls_sr, key=lambda x: x[0]*x[0]+x[1]*x[1]+x[2]*x[2])

    p = len(pxls_sr)//k
    for i in range(k):
        print(f"e({i}) pixel: {pxls_sr[p*i][0:3]}, index {pxls_sr[p*i][3]}")    

if __name__ == "__main__":
    main()