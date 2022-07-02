
def is_new_result(r1, r2):
    if r1[0] <= r2[0] and r1[0]+r1[1] >= r2[0]+r2[1]:
        return False
    return True

def get_succ_dup_lines(lines):
    res = list()
    reps = list()
    dup_index = 0
    dup_flag = False
    for i in range(len(lines)):
        dup_index = 0
        dup_flag = False
        j = 0
        if str.strip(lines[i]) == '':
            continue
        for j in range(i+1,len(lines)):
            ln2 = str.strip(lines[j])
            ln1 = str.strip(lines[i+dup_index])
            if ln1 == ln2:
                dup_flag = True
                dup_index += 1
                continue
            else:
                dup_flag = False
                res,reps = append_new_result(lines, res, reps, dup_index, i, j)
                dup_index = 0
        if dup_flag:
            dup_flag = False
            res,reps = append_new_result(lines, res, reps, dup_index, i, j)
            dup_index = 0

    return res

def append_new_result(lines, res, reps, dup_index, i, j):
    if str.strip(lines[i+dup_index-1]) == '':
        j -= 1
        dup_index -= 1
    if dup_index > 3:
        r = (i+1, dup_index)
        r2 = (j-dup_index, dup_index)
        if len(res) == 0 or is_new_result(res[-1],r) and r not in reps:
            res.append(r)
        reps.append(r)
        reps.append(r2)
    return res, reps

def main():
    with open('./2015-Summer/program.txt','r') as f:
        lines = f.readlines()
    
    res = get_succ_dup_lines(lines)
    print(f"Number: {len(res)}")
    print(res)
    res_list = list()
    for r in res:
        ln_res = ""
        for i in range(r[1]):
            ln_res += lines[r[0]+i-1]
        if ln_res not in res_list:
            res_list.append(ln_res)
    
    for r in res_list:
        print("---")
        print(str.strip(r))
        
    
if __name__ == "__main__":
    main()