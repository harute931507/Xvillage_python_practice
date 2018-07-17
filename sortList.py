import random


def gernerateList(num):
    result = [[random.randint(0, 9) for i in range(num)]for j in range(num)]
    return result


def displayList(data):
    for i in range(0, len(data)):
        print(data[i])
    print("")


num = 10
data = gernerateList(num)
displayList(data)
data.sort()
displayList(data)
