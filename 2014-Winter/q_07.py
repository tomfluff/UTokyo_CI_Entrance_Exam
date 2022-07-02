'''
n1 = A*(10^a)
n2 = B*(10^b)
n1*n2 = A*(10^a)*B*(10^b)
      = A*B*(10^a)*(10^b)
      = A*B*(10^(a+b))
      = A*B a+b
'''
import math

def get_mul_of_dec(a,b):
    res = "0"
    i = j = 0
    for e1 in a[::-1]:
        j = 0
        for e2 in b[::-1]:
            r = int(e1) * int(e2)
            zeros = '0' * (i+j)
            r_s = str(r) + zeros
            res = get_sum_of_dec(r_s, res)
            j += 1
        i += 1
    c = True if len(res) >= len(a)+len(b) else False
    return (res, c)

def get_sum_of_dec(a,b):
    if len(a) >= len(b):
        a_rev = a[::-1]
        b_rev = b[::-1]
    else:
        a_rev = b[::-1]
        b_rev = a[::-1]
    res = ""
    i = 0
    c = 0
    for d in a_rev:
        if i >= len(b_rev):
            b_n = 0
        else:
            b_n = int(b_rev[i])
        r = int(d) + b_n + c
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

def root_of_5_dec():
    a = ""
    for e in str(math.sqrt(5)):
        if not e.isdigit():
            continue
        a += e

    return a

def get_abs_sub_of_dec(a,b):
    a_rev = a[::-1]
    b_rev = b[::-1]
    
    res = ""
    i = 0
    c = 0
    for d in a_rev:
        if i >= len(b_rev):
            b_n = 0
        else:
            b_n = int(b_rev[i])
        r = int(d) - b_n - c
        if r < 0:
            r = 10 + r
            c = 1
        else:
            c = 0
        res += str(r)
        i += 1
    
    if c != 0:
        res += str(c)

    return res[::-1]

def get_mul_of_float(a, b):
    A = a.split(sep=' ')
    B = b.split(sep=' ')
    num1,c = get_mul_of_dec(A[0],B[0])
    num2 = get_sum_of_dec(A[1], B[1])
    if c:
        num2 = get_sum_of_dec(num2, '01')
    if num1[0] == '0' and num2 != '00':
        num1 = num1[1:]
        num2 = get_abs_sub_of_dec(num2, '01')
    res = num1[:32] + " " + num2
    return res

def get_phi():
    a = root_of_5_dec()
    a = get_sum_of_dec(a, '1'+'0'*(len(a)-1))
    a = a + '0'*(32-len(a))
    a = a +' 00'
    b = '05' + '0'*(30) + ' 00'
    phi = get_mul_of_float(a, b)
    return phi


def main():
    # 2, 4, 8, 16, 32, 64, 128
    # 128x8 -> 136x4 := 140
    # a^n * a^m = a^(n+m)
    #
    # 1/sqrt(5) := sqrt(5)/5 := 0.2 * sqrt(5)
    phi = get_phi()
    mem = [phi]

    res = phi
    for _ in range(7):
        res = get_mul_of_float(res, res)
        mem.append(res)
    # we have phi^128
    res = get_mul_of_float(res, mem[3])
    res = get_mul_of_float(res, mem[2])
    root_5 = root_of_5_dec() + " 00"
    res = get_mul_of_float(res, root_5)
    res = get_mul_of_float(res, "02" + "0" * 30 + " 00")

    print(res)
    

if __name__ == "__main__":
    main()
