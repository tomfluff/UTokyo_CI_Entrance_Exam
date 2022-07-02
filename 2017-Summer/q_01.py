from locale import atoi


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

def main():
    n = '012547896583214560'
    with open('2017-Summer/out1.txt','w') as f:
        for j in range(len(txt_nums[0])):
            for s in n:
                i = atoi(s)
                f.write(f"{txt_nums[i][j]}  ")
            f.writelines('\n')


if __name__ == "__main__":
    main()