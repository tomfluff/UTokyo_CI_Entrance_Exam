
def split_formula(formula, sep='+'):
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
        
        # formula analysis
        res = False
        for s in splt_form:
            temp_res = True
            for e in str.split(s, sep='&'):
                if e[0] == '!':
                    temp_res = temp_res and not var_dict[e[1:]]
                else:
                    temp_res = temp_res and var_dict[e]
            res = res or temp_res
        # ----

        if res:
            is_found = True
            print(var_dict)
    if not is_found:
        print('none')

def main():
    formula1 = "a+!b"

    find_all_solutions(formula1)

    

if __name__ == "__main__":
    main()