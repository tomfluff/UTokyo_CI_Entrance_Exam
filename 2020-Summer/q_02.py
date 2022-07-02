
# Note: They have a mistake in the fefinitions of the question, they say repeat in decending order.
# But based on the logic of the next question and the example they give, it's asceding order.
# so instead of p -> ... -> p-d+1 it should be p-d -> ... -> p

bZERO = (0).to_bytes(1,'big')

def main():
    w_buff = []
    with open('2020-Summer/data2.bin','rb') as f:
        EOF = False
        while not EOF:
            r = f.read(1)
            if r == b'':
                EOF = True
                continue

            if r != bZERO:
                print(f"Writing {r}")
                w_buff.append(r)
            else:
                p = int.from_bytes(f.read(1),'big')
                d = int.from_bytes(f.read(1),'big')
                print(f"Zero detected, p={p}, d={d}")
                if d == 0:
                    w_buff.append(bZERO)
                else:
                    for i in range(p-d,p):
                        w_buff.append(w_buff[i])
                        print(f"Writing {w_buff[i]}")
    
    with open('2020-Summer/data2_s.txt', 'wb') as f_out:
        for b in w_buff:
            f_out.write(b)

if __name__ == "__main__":
    main()