import re
import numpy as np
import matplotlib.pyplot as plt


def get_tuples_from_file(file_path) -> list:
    tuple_list = list()

    with open(file_path,'r') as f:
        for line in f:
            line = str.strip(line)
            numbers = re.findall('\d+', line)
            tuple_list.append([int(x) for x in numbers])
    
    return tuple_list


def seperate_tiples_into_axis(tuple_list, num_axis=2):
    axis = [list() for _ in range(num_axis)]
    for it in tuple_list:
        for i in range(len(it)):
            axis[i].append(it[i])
    
    return axis


def plot_tuples(tuple_list):
    x_axis, y_axis = seperate_tiples_into_axis(tuple_list)
    plt.plot(x_axis, y_axis, 'ro')
    plt.show()


def main():
    file_path = 'data1.txt'

    tuple_list = get_tuples_from_file(file_path)
    plot_tuples(tuple_list)
    

if __name__ == "__main__":
    main()