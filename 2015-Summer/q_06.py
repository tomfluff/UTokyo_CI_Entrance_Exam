

def is_relatively_similar(ln1, ln2) -> bool:
    l1 = str.strip(ln1)
    l2 = str.strip(ln2)
    if abs(len(l1) - len(l2)) > 4:
        return False
    if l1 == l2:
        return False

    steps = r_check_min_sim_steps(l1, l2, 0)

    if steps > 4:
        return False
    
    return True

def r_check_min_sim_steps(l1, l2, d):
    if d > 4:
        return 1
    if len(l1) == 0:
        return len(l2)
    if len(l2) == 0:
        return len(l1)
    
    if l1[0] == l2[0]:
        return r_check_min_sim_steps(l1[1:], l2[1:], d)
    
    # replace, remove, add
    l1_rep = l2[0]+l1[1:]
    l1_rem = l1[1:]
    l1_add = l2[0]+l1
    return 1 + min(r_check_min_sim_steps(l1_rep,l2, d+1), r_check_min_sim_steps(l1_rem,l2, d+1), r_check_min_sim_steps(l1_add,l2, d+1))

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
            is_sim = is_relatively_similar(ln1, ln2)
            if is_sim:
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