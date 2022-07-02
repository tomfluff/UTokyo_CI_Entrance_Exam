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


def generate_data_for_func(func, args, limit_x=30):
    point_list = list()
    for x in range(limit_x):
        y_val = func(args,x)
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


def main():
    file_path = '2012-Winter/data1.txt'
    tuple_list = get_tuples_from_file(file_path)
    a,b = calc_ab_from_data(tuple_list)
    data_list = generate_data_for_func(lambda args, x: args[0] * x + args[1], [a, b])

    x_axis = data_list[:,0]
    y_axis = data_list[:,1]

    dx_axis = tuple_list[:,0]
    dy_axis = tuple_list[:,1]

    plt.plot(x_axis, y_axis, 'ro')
    plt.plot(dx_axis, dy_axis, 'kx')
    plt.show()


if __name__ == "__main__":
    main()

