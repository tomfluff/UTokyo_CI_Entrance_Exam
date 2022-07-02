'''
n1 = A*(10^a)
n2 = B*(10^b)
n1*n2 = A*(10^a)*B*(10^b)
      = A*B*(10^a)*(10^b)
      = A*B*(10^(a+b))
      = A*B a+b
'''
import math
import numpy as np

def f_dyn(x):
    mem = ['0' for i in range(x)]
    mem[0] = '1'
    if x > 1:
        mem[1] = '1'
    for i in range(3,x+1):
        r = get_sum_of_dec(mem[i-2], mem[i-3])
        mem[i-1] = r
    
    return mem

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

def get_abs_sub_of_float(a,b):
    A = a.split(sep=' ')
    B = b.split(sep=' ')

    num1 = num2 = '0'
    comp_res = compare_dec_a_b(A[1], B[1])
    if comp_res > 0:
        while comp_res > 0:
            B[0] = '0' + B[0:31]
            B[1] = get_sum_of_dec(B[1], '01')
    elif comp_res < 0:
        while comp_res < 0:
            A[0] = '0' + A[0:31]
            A[1] = get_sum_of_dec(A[1], '01')
    
    assert compare_dec_a_b(A[1], B[1]) == 0

    if compare_dec_a_b(A[0], B[0]) >= 0:
        num1 = get_abs_sub_of_dec(A[0], B[0])
    else:
        num1 = get_abs_sub_of_dec(B[0], A[0])
    num2 = '00'
    
    while num1[0] != '0':
        num1 = num1[1:] + '0'
        num2 = get_abs_sub_of_dec(num2, '01')
    
    return num1 + " " + num2

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


def g_x_dyn(x):
    phi = get_phi()
    mem = [phi]
    ress = []

    for i in range(1,x):
        res = get_mul_of_float(mem[-1], phi)
        mem.append(res)

    root_5 = root_of_5_dec() + " 00"
    for e in mem:
        res = get_mul_of_float(e, root_5)
        res = get_mul_of_float(res, "02" + "0" * 30 + " 00")
        ress.append(res)

    return ress

def convert_f_x(ff):
    pr = res = ""
    
    if len(ff) < 32:
        res = ff + "0"*(32-len(ff))
    else:
        res = ff[:32]
    pr = str(len(ff)-1)
    if len(pr) < 2:
        pr = "0" + pr
    return res + " " + pr

def compare_dec_a_b(a,b):
    for i in range(len(a)):
        if int(a[i]) == int(b[i]):
            continue
        return 1 if int(a[i]) > int(b[i]) else -1
    return 0

def main():
    x = 50
    f_x = f_dyn(x)
    g_x = g_x_dyn(x)

    max_dist = '0'*32 + ' ' + '00'

    for i in range(x):
        ff = f_x[i]
        ff = convert_f_x(ff)
        tmp = get_abs_sub_of_float(ff, g_x[i])
        
        if compare_dec_a_b(tmp.split(sep=' ')[1], max_dist.split(sep=' ')[1]) > 0:
            max_dist = tmp
        elif compare_dec_a_b(tmp.split(sep=' ')[0], max_dist.split(sep=' ')[0]) >= 0:
            max_dist = tmp
        
    print(max_dist)


if __name__ == "__main__":
    main()
