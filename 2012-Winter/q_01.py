import re

def get_tuples_from_file(file_path) -> list:
    tuple_list = list()

    with open(file_path,'r') as f:
        for line in f:
            line = str.strip(line)
            numbers = re.findall('\d+', line)
            tuple_list.append([int(x) for x in numbers])
    
    return tuple_list


def get_max_tuple_from_list(tuple_list, value_index=0) -> tuple:
    assert len(tuple_list) > 0

    max_tuple = tuple_list[0]
    for it in tuple_list:
        if it[value_index] >= max_tuple[value_index]:
            max_tuple = it
    
    return max_tuple


def main():
    file_path = 'data1.txt'

    tuple_list = get_tuples_from_file(file_path)
    max_y_tuple = get_max_tuple_from_list(tuple_list, 1)

    print(max_y_tuple)


if __name__ == "__main__":
    main()