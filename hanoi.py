count = 0

def hanoi(n, a, b, c):

    global count
    
    if n == 1:
        count += 1
        print(count,a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        hanoi(1    , a, b, c)
        hanoi(n - 1, b, a, c)


hanoi(5, 'A', 'B', 'C')