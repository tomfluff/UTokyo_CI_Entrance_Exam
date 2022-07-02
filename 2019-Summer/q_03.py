
from locale import atoi

WHITE = (255,255,255)

def main():
    lines = []
    pxls = []
    width = 0
    with open('2019-Summer/image1.txt', 'r') as f:
        lines = f.readlines()
    
    # Assume file is a one-line file
    for l in lines:
        ns = [atoi(x) for x in l.strip().split(' ')]
        for i in range(0,len(ns),3):
            pxls.append((ns[i],ns[i+1],ns[i+2],i//3))
    
    pxls_sr = sorted(pxls, key=lambda x: x[3], reverse=True)
    pxls_sr = sorted(pxls_sr, key=lambda x: x[0]*x[0]+x[1]*x[1]+x[2]*x[2])
    
    print(f"N/2th pixel: {pxls_sr[len(pxls_sr)//2][0:3]}, index {pxls_sr[len(pxls_sr)//2][3]}")

if __name__ == "__main__":
    main()