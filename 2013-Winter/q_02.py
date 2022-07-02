
def split_formula(formula):
    form_splt = str.split(formula, sep='+')
    return form_splt

def gather_variables(formula):
    vars = dict()
    for c in str.lower(formula):
        if c.isalpha():
            vars[c] = False
    return vars

def find_all_solutions(formula):
    var_dict = gather_variables(formula)
    splt_form = split_formula(formula)
    is_found = False

    for i in range(2**len(var_dict)):
        for k in var_dict.keys():
            var_dict[k] = 1 & i
            i = i >> 1
        
        res = False
        for s in splt_form:
            temp_res = True
            for e in str.split(s, sep='&'):
                temp_res = temp_res and var_dict[e]
            res = res or temp_res
        
        if res:
            is_found = True
            print(var_dict)
    if not is_found:
        print('none')

def main():
    formula = "a+b"

    find_all_solutions(formula)

    

if __name__ == "__main__":
    main()