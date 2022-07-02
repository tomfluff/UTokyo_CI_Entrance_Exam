
def get_sum_of_dec(a,b):
    res = ""
    a_rev = a[::-1]
    b_rev = b[::-1]
    i = 0
    c = 0
    for d in a_rev:
        r = int(d) + int(b_rev[i]) + c
        if r > 9:
            r = r % 10
            c = 1
        else:
            c = 0
        res += str(r)
        i += 1
    
    if c != 0:
        res += str(c)

    return res[::-1]



def main():
    a = "00123456789012345678901234567890"
    b = "09876543210987654321098765432100"

    res = get_sum_of_dec(a,b)
    begin = True
    for e in res:
        if e != '0':
            begin = False
        if begin:
            continue
        print(e,end='')
    print()


if __name__ == "__main__":
    main()