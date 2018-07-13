def MxM_multiplication1(m, n):
    for i in range(1, m+1):
        for j in range(1, n+1):
            print(i, "x", j, "=", i*j, end="\t")
        print("\t")
    return

def MxM_multiplication2(m, n):
    for i in range(1, m+1):
        for j in range(1, n+1):
            print(j, "x", i, "=", i*j, end="\t")
        print("\t")
    return

def get_input():
    global row, col, mode

    while True:
        try:
            row = int(input("row number ? "))
            break
        except:
            print("please input integer. ")

    while True:
        try:
            col = int(input("col number ? "))
            break
        except:
            print("please input integer. ")

    while True:
        try:
            mode = input("> or v ? ")
            break
        except:
            print("please input > or v. ")

# Init
row = 0
col = 0
mode = ""

def main():
    get_input()

    functions = {
        '>': MxM_multiplication1,
        'v': MxM_multiplication2
    }

    func = functions[mode]
    
    func(row, col)

main()
