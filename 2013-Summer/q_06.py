import os


class L_statement():
    def __init__(self, type, p1, p2) -> None:
        self.type = type
        self.oper = [p1, p2]
    
    def get_oper(self, index = 0):
        return self.oper[index]

    
class L_program():
    def __init__(self) -> None:
        self.vars = [dict()]
        self.statements = list()
        self.curr_ln = 0
        self.past_ln = 0
    

    def add_statement(self, type, p1, p2):
        # check validity of type,p1,p2
        self.statements.append(L_statement(type, p1, p2))


    def check_and_get_var(self, var, method=0) -> int:
        val = 0
        if method == 0:
            if not str.isalpha(var) or var not in self.vars[-1]:
                raise Exception(f"Variable {var} illegal or not defined")
            return self.vars[-1][var]
        if method == 1:
            if str.isalpha(var):
                if var not in self.vars[-1]:
                    raise Exception(f"Variable {var} not defined")
                val = self.vars[-1][var]
            else:
                val = int(var)
            return val
        if method == 2:
            if not str.isalpha(var):
                raise Exception(f"Variable {var} illegal")
            return 0
    

    def next_line(self) -> bool:
        stsmt = self.statements[self.curr_ln]
        type = stsmt.type
        
        if type == "ADD":
            self.check_and_get_var(stsmt.get_oper(1))
            addition = self.check_and_get_var(stsmt.get_oper(0), 1)

            self.vars[-1][stsmt.get_oper(1)] += addition
            self.curr_ln += 1
        
        elif type == "CMP":
            vals = [0,0]
            vals[0] = self.check_and_get_var(stsmt.get_oper(0), 1)
            vals[1] = self.check_and_get_var(stsmt.get_oper(1), 1)
            
            if vals[0] == vals[1]:
                self.curr_ln += 2
            else:
                self.curr_ln += 1
        
        elif type == "JMP":
            jump_size = 0

            jump_size = self.check_and_get_var(stsmt.get_oper(0), 1)
            self.curr_ln += jump_size
        
        elif type == "PRN":
            vals = [0,0]
            vals[0] = self.check_and_get_var(stsmt.get_oper(0), 1)
            vals[1] = self.check_and_get_var(stsmt.get_oper(1), 1)
            
            print(vals[0], vals[1])
            return True
        
        elif type == "SET":
            val = 0
            self.check_and_get_var(stsmt.get_oper(0), 2)
            
            val = self.check_and_get_var(stsmt.get_oper(1), 1)
            self.vars[-1][stsmt.get_oper(0)] = val
            self.curr_ln += 1
        
        elif type == "SUB":
            go_to = self.check_and_get_var(stsmt.get_oper(0), 1)

            self.past_ln = self.curr_ln
            self.curr_ln = self.curr_ln + go_to
        
        elif type == "BAK":
            self.curr_ln = self.past_ln
        
        elif type == "CAL":
            go_to = self.check_and_get_var(stsmt.get_oper(0), 1)
            in_val = self.check_and_get_var(stsmt.get_oper(1), 1)
            self.vars.append({"in": in_val})

            self.past_ln = self.curr_ln
            self.curr_ln = self.curr_ln + go_to
        
        elif type == "RET":
            ret = self.check_and_get_var(stsmt.get_oper(0), 1)
            self.vars.pop()
            self.vars[-1]["out"] = ret

            self.curr_ln = self.past_ln

        else:
            raise Exception(f"Unknown instruction type {type}.")
        
        if self.curr_ln >= len(self.statements):
            return True
        else:
            return False


def read_instruction_file(filepath, L_prog = None) -> L_program:
    if L_prog is None:
        L_prog = L_program()

    with open(filepath, 'r') as f:
        for line in f:
            clean_line = str.strip(line)
            elements = clean_line.split(sep=' ')
            # [0] -> StatementType, [1] -> a, [2] -> b
            assert len(elements) == 3
            L_prog.add_statement(elements[0], elements[1], elements[2])

    return L_prog


def main():
    filepath = os.path.join("2013-Summer","prog3.txt")

    print(filepath)
    L_lang = read_instruction_file(filepath)
    print(len(L_lang.statements))
    
    go_on = True
    while go_on == True:
        go_on = not L_lang.next_line()


if __name__ == "__main__":
    main()
