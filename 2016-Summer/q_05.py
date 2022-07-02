'''
2015 -> MMXV
2015 / 1000 = 2 (15)
MM
15 / 10 = 1 (5)
MMX
5 / 5 = 1 (0)
MMXV
'''


def dec_to_rom(n) -> str:
    res = ""
    rom_lst = [('M',1000), ('CM',900), ('D',500), ('CD',400), ('C',100), ('XC',90), ('L',50), ('XL',40), ('X', 10), ('IX',9), ('V',5), ('IV', 4), ('I',1)]
    for r,v in rom_lst:
        n_div = n // v
        n_mod = n % v

        res += r*n_div
        n = n_mod

        if n == 0:
            return res


def main():
    n = 1066
    print(dec_to_rom(n))

if __name__ == "__main__":
    main()
