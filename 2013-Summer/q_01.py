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
    
    def add_statement(self, type, p1, p2):
        # check validity of type,p1,p2
        self.statements.append(L_statement(type, p1, p2))


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
    L_lang = read_instruction_file(filepath)

    # print the first operand
    for stsmt in L_lang.statements:
        print(stsmt.oper[0])


if __name__ == "__main__":
    main()
