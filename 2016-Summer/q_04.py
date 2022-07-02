
def rom_conv(c):
    rom_dic = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
    assert c in rom_dic
    return rom_dic[c]

def rom_check_lt(c1, c2) -> bool:
    if rom_conv(c1) < rom_conv(c2):
        return True
    return False

def get_next_roman_sec(n):
    if len(n) > 1 and rom_check_lt(n[0],n[1]):
        return n[0:2]
    return n[0]

def rom_to_dec(n) -> int:
    res = 0
    while n != '':
        c = get_next_roman_sec(n)
        res += rom_conv(c)
        n = n[len(c):]
    
    return res

def main():
    n = "MCMIV"
    print(rom_to_dec(n))

if __name__ == "__main__":
    main()
