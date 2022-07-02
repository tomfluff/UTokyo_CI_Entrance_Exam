
def get_letters_by_usage_from_file(f):
    lls = dict()
    for l in f.readlines():
        for w in l.lower():
            for c in w:
                if c in lls:
                    lls[c] += 1
                else:
                    lls[c] = 1
    return lls

def main():
    en_w = de_w = dict()

    with open('2020-Summer/data4.txt', 'r') as f:
        en_w = get_letters_by_usage_from_file(f)
    with open('2020-Summer/data4dict.txt', 'r') as f:
        de_w = get_letters_by_usage_from_file(f)

    sll_e = []
    for k in en_w:
        sll_e.append((k,en_w[k]))
    sll_d = []
    for k in de_w:
        sll_d.append((k,de_w[k]))

    sll_e.sort(key=lambda x: x[1], reverse=True)
    sll_d.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(sll_e)):
        print(f"#{sll_e[i][1]} '{sll_e[i][0]}' , '{sll_d[i][0]}'")
    # use the printed information to understand the encryption by hand

if __name__ == "__main__":
    main()