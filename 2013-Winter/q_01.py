

def split_formula(formula):
    form_splt = str.split(formula, sep='+')
    return form_splt

def main():
    formula = "a&b+c+a&c"

    splt = split_formula(formula)

    for f in splt:
        print(f)
    

if __name__ == "__main__":
    main()