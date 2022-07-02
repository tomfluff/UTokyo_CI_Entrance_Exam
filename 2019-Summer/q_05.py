
from locale import atoi


def p_distance(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2])

def find_cluster_index(p, clus_arr):
    best_c = 0
    best_d = 3*255
    for i in range(len(clus_arr)):
        d = p_distance(p,clus_arr[i])
        if d < best_d:
            best_d = d
            best_c = i
    
    return best_c

def get_inital_representatives(pxls,k):
    pxls.reverse()
    pxls_sr = sorted(pxls, key=lambda x: x[0]*x[0]+x[1]*x[1]+x[2]*x[2])
    pxls.reverse()

    p = len(pxls_sr)//k
    rps = []
    for i in range(k):
        rps.append(pxls_sr[p*i])
    
    return rps

def find_next_representatives(pxls, cens):
    repr = []
    for c in cens:
        best_d = 255*3
        best_p = -1
        for i in range(len(pxls)):
            d = p_distance(pxls[i],c)
            if d < best_d:
                best_d = d
                best_p = i
            elif d == best_d:
                if pxls[i][3] > pxls[best_p][3]:
                    best_p = i
        repr.append(pxls[best_p])
    return repr


# Can make this whole faster by using numpy, should consider upgrading
def main():
    pxls = []
    k = 128
    iter_lm = 10

    lines = []
    with open('2019-Summer/image1.txt', 'r') as f:
        lines = f.readlines()
    
    for l in lines:
        ns = [atoi(x) for x in l.strip().split(' ')]
        for i in range(0,len(ns),3):
            pxls.append((ns[i],ns[i+1],ns[i+2],i//3))
    
    repr = get_inital_representatives(pxls,k)

    for i in range(iter_lm+1):
        cens = [(0,0,0) for _ in repr]
        cens_i = [list() for _ in repr]
        n_check = len(pxls)
        for px in pxls:
            c_i = find_cluster_index(px,repr)
            cens_i[c_i].append(px[3])
        for i in range(len(cens)):
            for j in cens_i[i]:
                cens[i] = (cens[i][0]+pxls[j][0]/len(cens_i[i]), cens[i][1]+pxls[j][1]/len(cens_i[i]), cens[i][2]+pxls[j][2]/len(cens_i[i]))
            n_check -= len(cens_i[i])
        assert n_check == 0
        # find new reps
        repr = find_next_representatives(pxls, cens)
    for i in range(len(repr)):
        if i in [40,80,120]:
            print(f"p(i={i}): {repr[i]}")

if __name__ == "__main__":
    main()