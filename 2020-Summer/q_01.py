
# I thought that the file is in bits, but it seems like it is actually test
# ABC... etc, based on the definition in the question.
# So this code is not relevant to the question
class BitsRead(object):
    def __init__(self, f) -> None:
        self._file = f
    
    def read(self, n, l):
        k = l
        print(f"Readinng {n//8+l//8+min(l%8,1)} bytes...")
        rd = self._file.read(n//8+l//8+min(l%8,1))
        print(len(rd))
        # from first byte
        print(f"Starting with {8-n%8} bits from byte {n//8} shift {n%8}, using mask {bin(2**(8-n%8)-1)}")
        b = rd[n//8-1] & (2**(8-n%8)-1)
        k -= 8-n%8
        if k < 0:
            print(f"Need to trim result by shifting {abs(k)} bits")
            b = b >> abs(k)
            return b
        # middle part
        rs, re = n//8+1, n//8+k//8+1
        for i in range(rs,re):
            print(f"Adding 8 bits using byte {i}")
            b = b << 8
            b = b | rd[i-1]
            k -= 8
        # from end byte
        if k%8 != 0:
            print(f"Adding additional final {k%8} bits from byte {re} by shifting {8-k%8} bits")
            b = b << k%8
            b = b | (rd[re-1] >> (8-k%8))
        return b



def main():
    n = 310 # index (from)
    l = 11 # length (bits)
    bts = []
    with open('2020-Summer/data1.txt','rb') as f:
        if False:
            br = BitsRead(f)
            rd = br.read(n,l)
            print(bin(rd))
        else:
            r = f.read(1)
            rb = 0
            while r != b'':
                if r >= b'A' and r <= b'z':
                    rb = (int.from_bytes(r, 'big') - ord('A')).to_bytes(1,'big')
                elif r >= b'0' and r <= b'9':
                    rb = (int.from_bytes(r, 'big') - ord('0')).to_bytes(1,'big')
                elif r == b'@':
                    rb = (2**6-2).to_bytes(1,'big')
                else:
                    rb = (2**6-1).to_bytes(1,'big')
                bts.append(rb)
                r = f.read(1)
        for _b in bts[n//8:n//8+l//6+min(l%6,1)+1]:
            print(f"{int.from_bytes(_b,'big'):06b}",end='')
        print(f"\n{' '*(n%6)}^{'-'*(l-1)}")
                

if __name__ == "__main__":
    main()