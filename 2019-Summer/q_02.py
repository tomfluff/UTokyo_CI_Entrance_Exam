
from locale import atoi

WHITE = (255,255,255)

def get_image_width(pxls, width_op):
    width = 0
    for w in width_op:
        b_is_width = True
        for i in range(w-1,len(pxls),w):
            if pxls[i] != WHITE:
                b_is_width = False
        if b_is_width:
            width = w
            break
    return width

def update_width_options(pxls, width_op):
    if pxls[-1] == WHITE:
        b_add = True
        for w in width_op:
            if len(pxls) % w == 0:
                b_add = False
                break
        if b_add:
            width_op.append(len(pxls))

def main():
    lines = []
    pxls = []
    width_op = []
    with open('2019-Summer/image1.txt', 'r') as f:
        lines = f.readlines()
    
    for l in lines:
        ns = [atoi(x) for x in l.strip().split(' ')]
        for i in range(0,len(ns),3):
            pxls.append((ns[i],ns[i+1],ns[i+2]))
            update_width_options(pxls, width_op)
    width = get_image_width(pxls, width_op)
    
    print(f"Width of image: {width}")

if __name__ == "__main__":
    main()