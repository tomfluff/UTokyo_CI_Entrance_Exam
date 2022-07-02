
def f(x):
    assert(x>=0)
    if x <= 2:
        return 1
    return f(x-1)+f(x-2)

def main():
    print(f(6))

if __name__ == "__main__":
    main()