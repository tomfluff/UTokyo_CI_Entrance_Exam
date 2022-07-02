def eng_conv(c):
    eng_dic = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
        'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,
        'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20,
        'thirty':30,'fourty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90,'hundred':100,'thousand':1000}
    assert (c in eng_dic)
    return eng_dic[c]

def eng_check_lt(c1, c2) -> bool:
    if eng_conv(c1) < eng_conv(c2):
        return True
    return False

def get_next_eng_sec(n):
    j = 0
    for i in range(1,len(n)):
        if eng_conv(n[i]) > eng_conv(n[j]):
            j = i
    if len(n) > 0:
        return n[0:j+1]
    else:
        return []

def eng_to_dec(n) -> int:
    res = 0
    while len(n) > 0:
        c = get_next_eng_sec(n)
        if len(c) > 1:
            res += eng_to_dec(c[:-1]) * eng_conv(c[-1])
        else:
            res += eng_conv(c[0])
        n = n[len(c):]
    
    return res

def main():
    n = "fifty four thousand three hundred twelve"
    # pre-processing
    n = str.replace(n, ' and ',' ')
    n = str.split(n,sep=' ')
    # conversion
    print(eng_to_dec(n))

if __name__ == "__main__":
    main()