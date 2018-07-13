import random


class Matrix:
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col
        self.value = [random.randint(0, 10)
                      for i in range(0, self.row * self.col)]

    def display(self):
        print("Matrix", self.name, "(%d, %d):" % (self.row, self.col))
        for i in range(0, self.row):
            for j in range(0, self.col):
                print(self.value[i*self.col+j], end="\t")
            print("")

    def __add__(self, other):
        print("========== %s + %s ==========" % (self.name, other.name))

        if self.row != other.row or self.col != other.col:
            return print("Matrixs' size should be in the same size")

        tmp = [x+y for (x, y) in zip(self.value, other.value)]

        for i in range(0, self.row):
            for j in range(0, self.col):
                print(tmp[i*self.col+j], end="\t")
            print("")

        print("Matrixs' size should be in the same size")

    def __sub__(self, other):
        print("========== %s - %s ==========" % (self.name, other.name))

        if self.row != other.row or self.col != other.col:
            return print("Matrixs' size should be in the same size")

        tmp = [x-y for (x, y) in zip(self.value, other.value)]

        for i in range(0, self.row):
            for j in range(0, self.col):
                print(tmp[i*self.row+j], end="\t")
            print("")

    def __mul__(self, other):
        print("========== %s * %s ==========" % (self.name, other.name))

        if self.col != other.row:
            print("MatrixA's col and MatrixB's row should be in the same size")
            return ("Error", self.row, other.col)

        tmp_list = [0 for i in range(0, self.row * other.col)]

        for i in range(0, self.row):
            for j in range(0, other.col):
                tmp = 0
                for k in range(0, self.col):
                    tmp += self.value[self.col * i + k] * \
                        other.value[other.col * k + j]
                tmp_list[other.col * i + j] = tmp

        for i in range(0, self.row):
            for j in range(0, other.col):
                print(tmp_list[i * other.col + j], end="\t")
            print("")

        return (tmp_list, self.row, other.col)


def transpose(data):
    print("========== the transpose of A * B ==========")
    tmp_list = data[0]
    if tmp_list == "Error":
        return print("MatrixA's col and MatrixB's row should be in the same size")
        
    row = data[1]
    col = data[2]
    tmp2 = [list(range(0,col)) for x in range(0,row)]

    for i in range(0, row):
        for j in range(0, col):
            tmp2[i][j] = tmp_list[col * i + j]

    for i in range(0, col):
        for j in range(0, row):
            print(tmp2[j][i], end="\t")
        print("")


def get_input(m):
    global row1, col1, row2, col2

    while True:
        try:
            if m == 1:
                row1 = int(input("Enter A Matrix's row : "))
            if m == 2:
                row2 = int(input("Enter B Matrix's row : "))
            break
        except:
            print("please input an integer. ")

    while True:
        try:
            if m == 1:
                col1 = int(input("Enter A Matrix's col : "))
            if m == 2:
                col2 = int(input("Enter B Matrix's col : "))
            break
        except:
            print("please input an integer. ")


def main():
    get_input(1)
    MA = Matrix('A', row1, col1)
    MA.display()

    get_input(2)
    MB = Matrix('B', row2, col2)
    MB.display()

    MA + MB
    MA - MB
    MC = MA * MB
    transpose(MC)


# Init
row1, col1, row1, col1 = 0, 0, 0, 0
main()
