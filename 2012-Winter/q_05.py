import re
import numpy as np
import matplotlib.pyplot as plt


def get_tuples_from_file(file_path):
    tuple_list = list()

    with open(file_path,'r') as f:
        for line in f:
            line = str.strip(line)
            numbers = re.findall('\d+', line)
            tuple_list.append([int(x) for x in numbers])
    
    return np.array(tuple_list, dtype='int32')


def generate_data_for_func(func, args, xm, limit_x=30):
    point_list = list()
    for x in range(limit_x):
        y_val = func(args,xm,x)
        point_list.append([x, y_val])
    
    return np.array(point_list, dtype='float')


def calc_ab_from_data(tuple_list):
    x = tuple_list[:,0]
    y = tuple_list[:,1]
    xy = x * y
    x_sqr = x ** 2

    N = np.size(tuple_list, axis=0)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(xy)
    sum_xx = np.sum(x_sqr)
    sq_sum_x = sum_x ** 2

    denom = N * sum_xx - sq_sum_x
    a = (N * sum_xy - sum_x * sum_y) / denom
    b = (sum_xx * sum_y - sum_xy * sum_x) / denom

    return a,b


def F_x(args, xm, x):
    if x < xm:
        return args[0,0] * x + args[0,1]
    else:
        return args[1,0] * x + args[1,1]


def calc_sum_of_sq_err(data_points, func):
    sum = 0
    for dp in data_points:
        sum += (dp[1] - func(dp[0])) ** 2

    return sum


def main():
    file_path = '2012-Winter/data2.txt'
    x_m = 10

    tuple_list = get_tuples_from_file(file_path)
    part_1 = tuple_list[(tuple_list[:,0] < x_m)]
    part_2 = tuple_list[(tuple_list[:,0] >= x_m)]
    a1,b1 = calc_ab_from_data(part_1)
    a2,b2 = calc_ab_from_data(part_2)

    sum_err = calc_sum_of_sq_err(tuple_list, lambda x: F_x(np.array([[a1, b1],[a2,b2]]), x_m, x))
    print(sum_err)


if __name__ == "__main__":
    main()

