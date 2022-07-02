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

def get_most_similar_char(char):
    best_score = 0
    best_match = -1
    if char.shape[1] < 4:
        return 1
    for k in range(len(txt_nums)):
        if k == 1:
            continue
        np_c = np.array([list(l) for l in txt_nums[k]], dtype='str')
        score = 0
        for i in range(np_c.shape[0]):
            for j in range(np_c.shape[1]):
                if char[i,j] == np_c[i,j]:
                    score += 1
        
        if score > best_score:
            best_score = score
            best_match = k
    
    return best_match



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


def get_vertical_idxs(lines):
    e_i = s_i = 0
    fn_v_i = max([len(l) for l in lines])
    v_idxs = []

    while s_i < fn_v_i:
        is_found = False
        for l in lines:
            if len(l)-1 < e_i:
                continue
            if l[e_i] not in [' ']:
                is_found = True
        if is_found:
            e_i += 1
        else:
            if s_i < e_i:
                v_idxs.append((s_i,e_i))
            s_i = e_i + 1
            e_i = s_i
    
    return v_idxs

def get_horizontal_idxs(lines,v_idxs):
    h_idxs = []
    for s,e in v_idxs:
        s_i = e_i = 0
        for l in lines:
            if l[s:e].strip() != '':
                e_i += 1
            if l[s:e].strip() == '' or e_i == len(lines):
                if s_i < e_i:
                    h_idxs.append((s_i,e_i))
                s_i = e_i + 1
                e_i = s_i
    return h_idxs

def main():
    lines = []
    with open('2017-Summer/out5.txt','r') as f:
        lines = f.readlines()

    v_idxs = get_vertical_idxs([l[:-1] for l in lines])
    h_idxs = get_horizontal_idxs([l[:-1] for l in lines], v_idxs)
    
    max_l = max([len(l) for l in lines])
    nums = np.array([list(l[:-1].ljust(max_l)) for l in lines], dtype='str')
    res = 0

    for i in range(len(v_idxs)):
        v_s,v_e = v_idxs[i]
        h_s,h_e = h_idxs[i]

        char = nums[h_s:h_e,v_s:v_e]
        n = get_most_similar_char(char)
        res += int(math.pow(10,len(v_idxs) - 1 - i)) * n
    
    print(res)


if __name__ == "__main__":
    main()