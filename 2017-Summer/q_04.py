import numpy as np
import math

zero = ['****',
        '|  |',
        '*  *',
        '|  |',
        '****']
one = ['*',
        '|',
        '*',
        '|',
        '*']
two = ['****',
        '   |',
        '****',
        '|   ',
        '****']
three = ['****',
        '   |',
        '****',
        '   |',
        '****']
four = ['*  *',
        '|  |',
        '****',
        '   |',
        '   *']
five = ['****',
        '|   ',
        '****',
        '   |',
        '****']
six = ['*   ',
        '|   ',
        '****',
        '|  |',
        '****']
seven = ['****',
        '   |',
        '   *',
        '   |',
        '   *']
eight = ['****',
        '|  |',
        '****',
        '|  |',
        '****']
nine = ['****',
        '|  |',
        '****',
        '   |',
        '   *']

txt_nums = [zero, one, two, three, four, five, six, seven, eight, nine]


def find_correct_index(lines, s_i):
    e_i = 0
    for i in range(len(lines)):
        l = lines[i]
        if l == '':
            continue
        n_e_i = str.find(l,' ',s_i)
        if n_e_i == -1:
            n_e_i = len(l)
        if n_e_i >= e_i:
            e_i = n_e_i
    return e_i

def get_int_from_repr_array(arr):
    if np.array_equal(arr, zero):
        return 0
    if np.array_equal(arr, one):
        return 1
    if np.array_equal(arr, two):
        return 2
    if np.array_equal(arr, three):
        return 3
    if np.array_equal(arr, four):
        return 4
    if np.array_equal(arr, five):
        return 5
    if np.array_equal(arr, six):
        return 6
    if np.array_equal(arr, seven):
        return 7
    if np.array_equal(arr, eight):
        return 8
    if np.array_equal(arr, nine):
        return 9

def get_idx_for_nums(lines):
    idxs = []
    s_i = 0
    final_si = max([len(l) for l in lines])

    while s_i < final_si:
        e_i = find_correct_index(lines, s_i)
        idxs.append((s_i,e_i))

        s_i = e_i
        n_s_i = s_i
        is_found = False
        while n_s_i < final_si and is_found == False:
            for l in lines:
                if n_s_i >= len(l):
                    continue
                if l[n_s_i] not in [' ','\n']:
                    is_found = True
                    s_i = n_s_i
            n_s_i += 1

    return idxs


def main():
    lines = []
    with open('2017-Summer/out3.txt','r') as f:
        lines = f.readlines()

    idxs = get_idx_for_nums([l[:-1] for l in lines])
    nums = np.full((len(idxs),5), fill_value="****", dtype='object')
    i = 0
    for s,e in idxs:
        j = 0
        for l in lines:
            if len(l) < s or l[s:e].strip() == '':
                continue
            nums[i,j] = l[s:e]
            j += 1
        i += 1

    num = 0
    i = len(idxs)
    for el in nums:
        num += int(math.pow(10,i-1)) * get_int_from_repr_array(el)
        i -= 1
    
    print(num)


if __name__ == "__main__":
    main()