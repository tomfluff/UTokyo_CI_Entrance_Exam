

def generate_data_for_func(func, args, limit_x=30) -> list:
    point_list = list()
    for x in range(limit_x):
        y_val = func(args,x)
        if y_val < 30 and int(y_val) == y_val:
            point_list.append([x, int(y_val)])
    
    return point_list


def generate_consol_display_data(ponit_data):
    consol_data = [0 for _ in range(30*30)]

    for dp in ponit_data:
        consol_data[(29 - dp[1])*30 + dp[0]] = 1

    for i in range(30):
        if consol_data[i*30] != 1:
            consol_data[i*30] = 2
        if consol_data[29*30 + i] != 1:
            consol_data[29*30 + i] = 3
    
    if consol_data[29*30] == 1:
        consol_data[29*30] = 4
    else:
        consol_data[29*30] = 5
    
    return consol_data


def translate_consol_indicator(dp):
    if dp == 0:
        return '  '
    if dp == 1:
        return ' x'
    if dp == 2:
        return ' |'
    if dp == 3:
        return '--'
    if dp == 4:
        return ' x'
    if dp == 5:
        return ' +'


def print_ascii_plot_to_consol(consol_data):
    print("30 |", end='')
    for i in range(len(consol_data)):
        if i % 30 == 0:
            if ((i//30) +1) % 10 == 0:
                print("\n%s" % (str(29 - (i//30)).ljust(2)), end='')
            else:
                print("\n  ", end='')
        print(translate_consol_indicator(consol_data[i]), end='')
    print("--")
    for i in range(31):
        if i == 0:
            print("   0", end='')
        elif i % 10 == 0:
            print(i, end='')
        else:
            print("  ", end='')
    print()


def main():
    # generate x_axis, y_axis
    a = 0.5
    b = 10

    data_list = generate_data_for_func(lambda args, x: args[0] * x + args[1], [a, b])

    # print to consol
    consol_data = generate_consol_display_data(data_list)
    print_ascii_plot_to_consol(consol_data)


if __name__ == "__main__":
    main()