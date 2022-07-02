import os


class L_statement():
    def __init__(self, type, p1, p2) -> None:
        self.type = type
        self.oper = [p1, p2]
    
    def get_oper(self, index = 0):
        return self.oper[index]

    
class L_program():
    def __init__(self) -> None:
        self.vars = dict()
        self.statements = list()
        self.curr_ln = 0
    
    def add_statement(self, type, p1, p2):
        # check validity of type,p1,p2
        self.statements.append(L_statement(type, p1, p2))
    
    def next_line(self) -> bool:
        stsmt = self.statements[self.curr_ln]
        type = stsmt.type
        if type == "ADD":
            addidion = 0
            if not str.isalpha(stsmt.get_oper(1)) or stsmt.get_oper(1) not in self.vars:
                raise Exception(f"Variable {stsmt.get_oper(0)} illegal or not defined")
            if str.isalpha(stsmt.get_oper(0)):
                if stsmt.get_oper(0) not in self.vars:
                    raise Exception(f"Variable {stsmt.get_oper(0)} not defined")
                addidion = self.vars[stsmt.get_oper(0)]
            else:
                addidion = int(stsmt.get_oper(0))
            self.vars[stsmt.get_oper(1)] += addidion
            self.curr_ln += 1
        elif type == "CMP":
            self.curr_ln += 1
            pass
        elif type == "JMP":
            self.curr_ln += 1
            pass
        elif type == "PRN":
            printing = [0,0]
            if str.isalpha(stsmt.get_oper(0)):
                if stsmt.get_oper(0) not in self.vars:
                    raise Exception(f"Variable {stsmt.get_oper(0)} not defined")
                printing[0] = self.vars[stsmt.get_oper(0)]
            else:
                printing[0] = int(stsmt.get_oper(0))
            if str.isalpha(stsmt.get_oper(1)):
                if stsmt.get_oper(1) not in self.vars:
                    raise Exception(f"Variable {stsmt.get_oper(1)} not defined")
                printing[1] = self.vars[stsmt.get_oper(1)]
            else:
                printing[1] = int(stsmt.get_oper(1))
            
            print(printing[0], printing[1])
            return True
        elif type == "SET":
            setting = 0
            if not str.isalpha(stsmt.get_oper(0)):
                raise Exception(f"Variable {stsmt.get_oper(0)} illegal")
            if str.isalpha(stsmt.get_oper(1)):
                if stsmt.get_oper(1) not in self.vars:
                    raise Exception(f"Variable {stsmt.get_oper(1)} not defined")
                setting = self.vars[stsmt.get_oper(1)]
            else:
                setting = int(stsmt.get_oper(1))
            self.vars[stsmt.get_oper(0)] = setting
            self.curr_ln += 1
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
    filepath = os.path.join("2013-Summer","prog1.txt")

    print(filepath)
    L_lang = read_instruction_file(filepath)
    print(len(L_lang.statements))
    
    go_on = True
    while go_on == True:
        go_on = not L_lang.next_line()


if __name__ == "__main__":
    main()
