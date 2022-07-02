
def main():
    with open('./2015-Summer/program.txt','r') as f:
        lines = f.readlines()
    
    cnt = 0
    for l in lines:
        cnt += l.count(';')

    print(f"number of ';' is: {cnt}")
    
if __name__ == "__main__":
    main()