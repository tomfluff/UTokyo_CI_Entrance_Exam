
def lru_insert(elm, lru, s):
    if len(lru) >= s:
        lru.pop()
    lru.insert(0,elm)

def lru_is_in(elm, lru):
    return elm in lru

def lru_refresh(elm,lru):
    lru.remove(elm)
    lru.insert(0,elm)

def main():
    cache_lru = []

    m = 6
    n = 4
    p = 2
    s = 8

    rds = 0 # number of readings

    u = 0
    while u < m:
        v = 0
        while v < m:
            w = 0
            while w < n:
                i = u
                while i < u+p:
                    j = v
                    while j < v+p:
                        k = w
                        while k < w+p:
                            if not lru_is_in((i+1)*n+k, cache_lru):
                                rds += 1
                                lru_insert((i+1)*n+k, cache_lru,s)
                            else:
                                lru_refresh((i+1)*n+k, cache_lru)
                            if not lru_is_in(-(k+1)*m-j, cache_lru):
                                rds += 1
                                lru_insert(-(k+1)*m-j, cache_lru,s)
                            else:
                                lru_refresh(-(k+1)*m-j, cache_lru)
                            k += 1
                        j += 1
                    i += 1
                w += p
            v += p
        u += p
    print(rds)

if __name__ == "__main__":
    main()