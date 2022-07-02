

def dec_to_rom(n) -> str:
    res = ""
    rom_lst = [('M',1000), ('IM',999), ('VM',995), ('XM', 990), ('LM', 950), ('CM',900), ('D',500), ('ID',499), ('VD',495), ('XD', 490), ('LD', 450), ('CD',400), ('C',100), ('IC',99), ('VC',95), ('XC',90), ('L',50), ('IL',49), ('VL',45), ('XL',40), ('X', 10), ('IX',9), ('V',5), ('IV', 4), ('I',1)]
    ignore_list = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV'] # because in the original definition there are ok [a = b]
    for r,v in rom_lst:
        n_div = n // v
        n_mod = n % v
        if len(res) > 0 and len(r) > 1 and res[-1] == r[-1] and r not in ignore_list:
            continue
        res += r*n_div
        n = n_mod

        if n == 0:
            return res


def main():
    n = 1066
    print(dec_to_rom(n))

if __name__ == "__main__":
    main()
