def lev(s1, s2):
    if s1 == s2:
        return 0
    elif len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)

    col = len(s1)
    row = len(s2)

    v1 = list(range(col + 1))
    v2 = [0 for i in range(col + 1)]

    for i in range(row):
        v2[0] = i + 1

        for j in range(col):
            tmp = 0 if s1[j] == s2[i] else 1
            v2[j + 1] = min(v2[j] + 1, v1[j + 1] + 1, v1[j] + tmp)

        v1 = v2[:]

    return v1[-1]

a = "12asoihlkn"
b = "asdh222"

print(lev(a, b))


#         string1
#         0   1   2   3 ...   len(string1)  ---> v1(1)
# s   0                                     ---> v2(1)  ---> v1(2)
# t   1                                                 ---> v2(2)  ---> v1(3)
# r   2                                                             ---> v2(3)
# i   3
# n   .
# g   .
# 2   .
#     len(string2)
    
