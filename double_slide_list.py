def double_slide_list(M, B, I):
    L = []
    if M - B > 0:
        I = -I

    l = range(M, B, I)

    L.extend(l)
    del L[0]
    L.reverse()
    L.extend(l)

    return L

test_data1 = [10, 24, 2]
test_data2 = [10, 4, 2]

T1 = double_slide_list(test_data1[0], test_data1[1], test_data1[2])
T2 = double_slide_list(test_data2[0], test_data2[1], test_data2[2])

print(T1)
print(T2)
