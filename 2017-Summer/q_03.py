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
    inp = '690,0,4,2,2,1'
    n = inp[:inp.find(',')]
    prnt_lines = []
    defs = str.split(inp[inp.find(',')+1:],',')
    with open('2017-Summer/out3.txt','w') as f:
        indt = 0
        for i in range(len(n)):
            dg = atoi(n[i])
            tp = atoi(defs[i*2])
            sp = atoi(defs[i*2+1]) if i*2+1 < len(defs) else 0
            for j in range(5):
                while len(prnt_lines)-1 < tp+j:
                    prnt_lines.append('')
                if len(prnt_lines[tp+j]) < indt:
                    prnt_lines[tp+j] += ' ' * (indt-len(prnt_lines[tp+j]))
                prnt_lines[tp+j] += txt_nums[dg][j] + ' ' * sp
            indt = max(len(prnt_lines[tp]),indt)

        for l in prnt_lines:
            f.write(l+'\n')

if __name__ == "__main__":
    main()
