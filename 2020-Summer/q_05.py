# Can also use 'factor' linux command

import primefac

def get_decomposition(n):
    return list(primefac.primefac(n))

def main():
    n = 3858843578360632069557337
    print(type(n))
    pq = get_decomposition(n)
    print(pq)

    # Using p and q we can compute d, then decrypt the file

if __name__ == "__main__":
    main()