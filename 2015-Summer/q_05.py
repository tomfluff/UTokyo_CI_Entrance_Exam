

def compare_lines(line1, line2):
    if len(line1) > len(line2):
        line2 = line2 + ' ' * (len(line1) - len(line2))
    else:
        line1 = line1 + ' ' * (len(line2) - len(line1))
    
    cnt = 0
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            cnt += 1
    
    return cnt

def get_similar_line_pairs(lines):
    res = list()
    for i in range(len(lines)):
        ln1 = str.strip(lines[i])
        if len(ln1) < 6:
            continue
        for j in range(i+1,len(lines)):
            ln2 = str.strip(lines[j])
            if len(ln2) < 6:
                continue
            sim_cnt = compare_lines(ln1, ln2)
            if sim_cnt > 0 and sim_cnt < 5:
                res.append((ln1,ln2))
    
    return res

def main():
    with open('./2015-Summer/program.txt','r') as f:
        lines = f.readlines()
    
    res = get_similar_line_pairs(lines)
    print(f"Number: {len(res)}")
    for r in res:
        print(f"'{r}'")
    
if __name__ == "__main__":
    main()