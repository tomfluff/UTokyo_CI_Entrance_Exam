
def count_element_in_lines(lines, elem=' ') ->int:
    cnt = 0
    linenum = list()
    ln = 0
    for l in lines:
        ln += 1
        tmp_cnt = l.count(elem)
        if tmp_cnt > 0:
            linenum.append(ln)
            cnt += tmp_cnt
    
    return (cnt, linenum)

def main():
    with open('./2015-Summer/program.txt','r') as f:
        lines = f.readlines()
    
    elem = 'main'
    main_cnt, main_ln = count_element_in_lines(lines, elem)

    print(f"number of '{elem}' is: {main_cnt}, in: {main_ln}")
    
if __name__ == "__main__":
    main()