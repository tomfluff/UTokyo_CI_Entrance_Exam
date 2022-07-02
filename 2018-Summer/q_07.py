import math 

def lru_insert(elm, lru, s):
    if len(lru) >= s:
        lru.pop()
    lru.insert(0,elm)

def lru_is_in(elm, lru):
    return elm in lru

def lru_refresh(elm,lru):
    lru.remove(elm)
    lru.insert(0,elm)

def get_p_options(m,n,s):
    return [x for x in range(2,int(math.sqrt(s/2))+1) if m % x == 0 and n % x == 0]

'''
Technically, it is enough to return the number of reads for the largest p suggestion.
Since if the entire sub-matrix cannot fit into s then there there will be much more reads.
But here I am checking all posiibilities.
'''
def main():
    cache_lru = []

    m = 200
    n = 150
    s = 600
    best_p = 1
    min_rds = m*n*m*2
    all_p = get_p_options(m,n,s)
    all_p.reverse()

    for p in all_p:
        rds = 0 # number of readings
        go_on = True
        u = 0
        while u < m and go_on:
            v = 0
            while v < m and go_on:
                w = 0
                while w < n and go_on:
                    i = u
                    while i < u+p and go_on:
                        j = v
                        while j < v+p and go_on:
                            k = w
                            while k < w+p and go_on:
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
                                if rds > min_rds:
                                    go_on = False
                                k += 1
                            j += 1
                        i += 1
                    w += p
                v += p
            u += p
        if rds < min_rds and p > best_p:
            best_p = p
            min_rds = rds
    
    print(f"best p={best_p} : {min_rds} readings")

if __name__ == "__main__":
    main()