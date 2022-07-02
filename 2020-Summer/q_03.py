
bZERO = (0).to_bytes(1,'big')

def get_max_match(buff, i):
    max_p = 0
    max_d = 0
    j = 0
    k = i
    d = 0
    while j < i+1:
        if buff[j] == buff[k]:
            j += 1
            k += 1
            d += 1
        else:
            if max_d < d:
                max_d = d
                max_p = j
            j = j - d + 1
            k = i
            d = 0
    return max_p, max_d

def compress_buffer(buff):
    comp_buff = []
    d = p = 0
    i = 0
    while i < len(buff):
        print(f"Checking for i={i} (from {len(buff)})")
        p,d = get_max_match(buff,i)
        if d < 4:
            if buff[i] == bZERO:
                comp_buff.append(bZERO)
                comp_buff.append(bZERO)
                comp_buff.append(bZERO)
            else:
                comp_buff.append(buff[i])
            i += 1
        else:
            comp_buff.append(int.to_bytes(0,1,'big'))
            comp_buff.append(int.to_bytes(p,1,'big'))
            comp_buff.append(int.to_bytes(d,1,'big'))
            i += d
    return comp_buff

def main():
    in_buff = []
    with open('2020-Summer/data2_s.txt', 'rb') as f:
        EOF = False
        while not EOF:
            r = f.read(1)
            if r == b'':
                EOF = True
                continue
            in_buff.append(r)
    
    comp_buff = compress_buffer(in_buff)

    with open('2020-Summer/data3.bin', 'wb') as f_out:
        for b in comp_buff:
            f_out.write(b)

if __name__ == "__main__":
    main()