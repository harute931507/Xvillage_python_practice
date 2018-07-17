def get_input():
    global N, X, mode1, mode2

    while True:
        try:
            N = float(input("N is ? "))
            break
        except:
            print("please input a number . ")

    while True:
        try:
            X = float(input("X is ? "))
            break
        except:
            print("please input a number . ")

    while True:
        try:
            mode1 = input("operator ? ")
            break
        except:
            print("please input +,-,*,/,** . ")

    while True:
        try:
            mode2 = input("operator ? ")
            break
        except:
            print("please input +,-,*,/,** . ")


def Function(mode):
    def fun1(X):
        return N + X

    def fun2(X):
        return N - X

    def fun3(X):
        return N * X

    def fun4(X):
        return N / X

    def fun5(X):
        return N ** X

    functions = {
        '+': fun1,
        '-': fun2,
        '*': fun3,
        '/': fun4,
        '**': fun5
    }
    
    return functions[mode]





# Init
N = 0
X = 0
mode1 = ""
mode2 = ""


def main():
    get_input()

    fun1 = Function(mode1)
    fun2 = Function(mode2)

    print(N, mode1, X, "=", fun1(X))
    print(N, mode2, X, "=", fun2(X))


main()
