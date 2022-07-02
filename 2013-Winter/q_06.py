import re

def split_formula(formula, sep='+'):
    form_splt = str.split(formula, sep='+')
    return form_splt

def gather_variables(formula):
    vars = dict()
    for c in str.lower(formula):
        if c.isalpha():
            vars[c] = False
    return vars

def get_parenthesis(formula):
    res = re.findall(pattern='\([0-1a-z+&!]+\)',string=formula)
    return res

def get_sub_cnf(vars) -> str:
    s = ""
    for k in vars.keys():
        if not vars[k]:
            s += k
        else:
            s = s + "!" + k
        s += "+"
    
    return s[:-1]

def eval_formula(formula, vars) -> bool:
    res = False
    for s in split_formula(formula):
        temp_res = True
        for e in str.split(s, sep='&'):
            if e.isdigit():
                if e == '0':
                    temp_res = False
                else:
                    temp_res = temp_res and True
            elif e[0] == '!':
                temp_res = temp_res and not vars[e[1:]]
            else:
                temp_res = temp_res and vars[e]
        res = res or temp_res
    return res

def find_all_solutions(formula):
    var_dict = gather_variables(formula)
    cnf = ""
    is_found = False

    for i in range(2**len(var_dict)):
        temp_formula = formula
        for k in var_dict.keys():
            if not k.isalpha():
                continue
            var_dict[k] = 1 & i
            i = i >> 1
        
        # formula analysis
        p_parts = get_parenthesis(temp_formula)
        while len(p_parts) > 0:
            for p in p_parts:
                val = eval_formula(p[1:-1],var_dict)
                if val:
                    temp_formula = str.replace(temp_formula,p,'1')
                else:
                    temp_formula = str.replace(temp_formula,p,'0')
            p_parts = get_parenthesis(temp_formula)
        res = eval_formula(temp_formula, var_dict)
        # ----

        if not res:
            print(var_dict)
            cnf += "(" + get_sub_cnf(var_dict) + ")" + "&"
    
    return cnf[:-1]

def main():
    formula1 = "!a&b&!c+a&!d"

    dnf = find_all_solutions(formula1)
    print(dnf)


if __name__ == "__main__":
    main()