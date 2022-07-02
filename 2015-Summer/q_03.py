
def get_duplicate_successive_lines(lines):
    res = list()
    prev_line = str.strip(lines[0])
    for i in range(1,len(lines)):
        if str.strip(lines[i]) == prev_line:
            if prev_line not in res:
                res.append(str.strip(lines[i]))
        prev_line = str.strip(lines[i])
    
    return res

def main():
    with open('./2015-Summer/program.txt','r') as f:
        lines = f.readlines()
    
    res = get_duplicate_successive_lines(lines)
    for r in res:
        print(f"'{r}'")
    
if __name__ == "__main__":
    main()