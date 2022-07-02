# Here I assume that file can be  weirdly formatted and matrix isn't defined in a single line.

def main():
    lines = []
    with open('2018-Summer/mat1.txt','r') as f:
        lines = f.readlines()

    rows = 0
    cols = 0

    cols_check = True
    rows_check = True
    for l in lines:
        sep_cnt = l.count(',')
        end_cnt = l.count('.')
        if sep_cnt > 0:
            rows += sep_cnt
            if cols_check:
                if l.find(',') > 0:
                    cols += len(l[:l.find(',')].strip().split(' '))
                cols_check = False
        else:
            if cols_check:
                cols += len(l.strip().split(' '))
        if end_cnt > 0:
            rows += 1
            break
        
    
    print(f"{rows} x {cols}")


if __name__ == "__main__":
    main()
