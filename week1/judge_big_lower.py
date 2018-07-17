def get_input():
    global a, b

    while True:
        try:
            a = float(input("a is ? "))
            break
        except:
            print("please input a number . ")

    while True:
        try:
            b = float(input("b is ? "))
            break
        except:
            print("please input a number . ")


# Init
a = 0
b = 0


def main():
    get_input()

    if a - b > 0:
        print("a > b")
    elif a-b < 0:
        print("a < b")
    else:
        print("a = b")


main()
