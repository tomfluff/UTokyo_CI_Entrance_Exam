import numpy as np
from locale import atoi

WHITE = (255,255,255)

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

def get_image_width(pxls, width_op):
    width = 0
    for w in width_op:
        b_is_width = True
        for i in range(w-1,len(pxls),w):
            if pxls[i][0:3] != WHITE:
                b_is_width = False
        if b_is_width:
            width = w
            break
    return width

def update_width_options(px, l, width_op):
    if px == WHITE:
        b_add = True
        for w in width_op:
            if l % w == 0:
                b_add = False
                break
        if b_add:
            width_op.append(l)

def LOGIT(msg):
    if True:
        print(f"LOG: {msg}")

def save_tif_image(fname, img, w, h):
    w3 = w&(2**8 -1)
    w2 = (w&(2**16 -1))>>8
    w1 = (w&(2**24 -1))>>16
    w0 = (w)>>24

    h3 = h&(2**8 -1)
    h2 = (h&(2**16 -1))>>8
    h1 = (h&(2**24 -1))>>16
    h0 = (h)>>24

    s = h*w*3
    s3 = s&(2**8 -1)
    s2 = (s&(2**16 -1))>>8
    s1 = (s&(2**24 -1))>>16
    s0 = (s)>>24
    
    hd_bytes = np.array([
        77,77,0,42,0,0,0,8,0,7,1,0,0,4,0,0,
        0,1,w0,w1,w2,w3,1,1,0,4,0,0,0,1,h0,h1,
        h2,h3,1,2,0,3,0,0,0,3,0,0,0,98,1,6,
        0,3,0,0,0,1,0,2,0,0,1,17,0,4,0,0,
        0,1,0,0,0,104,1,21,0,3,0,0,0,1,0,3,
        0,0,1,23,0,4,0,0,0,1,s0,s1,s2,s3,0,0,
        0,0,0,8,0,8,0,8], dtype='uint8')
    with open(fname, 'wb') as f:
        for b in hd_bytes:
            f.write(b)
        
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                for k in range(img.shape[2]):
                    f.write(img[i,j,k])

# Can make this whole faster by using numpy, should consider upgrading
def main():
    pxls = []
    k = 16
    iter_lm = 10
    width_op = []

    lines = []
    with open('2019-Summer/image3.txt', 'r') as f:
        lines = f.readlines()
    LOGIT("Reading file...")
    for l in lines:
        ns = [atoi(x) for x in l.strip().split(' ')]
        for i in range(0,len(ns),3):
            pxls.append((ns[i],ns[i+1],ns[i+2],i//3))
            update_width_options(pxls[-1][0:3],len(pxls), width_op)
    
    width = get_image_width(pxls, width_op)
    LOGIT(f"Image width: {width}")
    
    repr = get_inital_representatives(pxls,k)
    LOGIT(f"Searching for representations...")

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
    LOGIT(f"Calculated representation for k={k}")

    new_img = np.full((len(pxls)//width,width,3),dtype='uint8',fill_value=0)
    for i in range(new_img.shape[0]):
        for j in range(new_img.shape[1]):
            p_i = find_cluster_index(pxls[i*width+j],repr)
            for k in range(new_img.shape[2]):
                new_img[i,j,k] = repr[p_i][k]

    save_tif_image('2019-Summer/image_.tif', new_img, new_img.shape[1], new_img.shape[0])


if __name__ == "__main__":
    main()