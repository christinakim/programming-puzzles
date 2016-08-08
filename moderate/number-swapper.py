def numswap(a, b):
    a = a - b
    b = a + b
    a = b - a
    return a,b

def main():
    print numswap(3, 4)

if __name__ == '__main__':
    main()