# Here I assume matrix defined in a single line, so one line per matrix
from locale import atoi
import numpy as np

def get_mat_from_file(filename):
    mats = []
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    for l in lines:
        rows =  l.strip()[:-1].split(',')
        _r = len(rows)
        _c = len(rows[0].split(' '))
        mats.append(np.full((_r,_c),0))
        i = 0
        for ro in rows:
            j = 0
            for itm in ro.split(' '):
                mats[-1][i,j] = atoi(itm)
                j += 1
            i += 1
        
        return mats

def get_mul_mat_a_b(mat_a, mat_b):
    mat_c = np.matmul(mat_a,mat_b)
    return mat_c

def get_trace_for_mat(mat):
    return np.trace(mat)

def main():
    # According to the instructions there is no issues with using numpy
    mat_a = get_mat_from_file('2018-Summer/mat1.txt')[0]
    mat_b = get_mat_from_file('2018-Summer/mat2.txt')[0]
    mat_c = get_mul_mat_a_b(mat_a,mat_b)
    trc = get_trace_for_mat(mat_c)

    print(trc)
    

if __name__ == "__main__":
    main()