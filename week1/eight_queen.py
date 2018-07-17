def eight_queen(data):
    for i in range(0, len(data)):
        x = data[i][0]
        y = data[i][1]

        for j in range(i+1, len(data)):
            if data[j][0] == x:
                return print(False)
            if data[j][1] == y:
                return print(False)
            if data[j][0] == x+j and data[j][1] == y+j:
                return print(False)
            if data[j][0] == x+j and data[j][1] == y-j:
                return print(False)
    return print(True)


test_data = [
    [0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]]

eight_queen(test_data)
