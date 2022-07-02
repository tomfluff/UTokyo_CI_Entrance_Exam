
def get_duplicate_lines(lines):
    srt_ln = sorted(lines)
    res = list()

    prev_line = srt_ln[0]
    for i in range(1, len(srt_ln)):
        ln = str.strip(srt_ln[i])
        if ln != '' and ln == prev_line:
            if prev_line not in res:
                res.append(prev_line)
        else:
            prev_line = ln
    
    return res

def main():
    with open('./2015-Summer/program.txt','r') as f:
        lines = f.readlines()
    
    res = get_duplicate_lines(lines)
    print(f"Number: {len(res)}")
    for r in res:
        print(f"'{r}'")
    
if __name__ == "__main__":
    main()