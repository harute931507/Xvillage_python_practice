def get_input():
    global N

    while True:
        try:
            N = float(input("N is ? "))
            break
        except:
            print("please input a number . ")


def factor(n):
    if n == 1:
        return 1
    else:
        return n * factor(n-1)

def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# Init
N = 0


def main():
    get_input()
    print(factor(N))
    print(fib(N))


main()
