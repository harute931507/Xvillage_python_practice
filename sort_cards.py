def sort_cards_bad(data):
    result = []
    for i in data:
        tmp = []
        num = []
        jqk = []
        for j in i:
            try:
                int(j)
                num.append(int(j))
            except:
                jqk.append(j)

        num.sort()
        num = [str(x) for x in num]
        num.reverse()

        for k in jqk:
            if k == "A":
                tmp.append(k)
        for k in jqk:
            if k == "K":
                tmp.append(k)
        for k in jqk:
            if k == "Q":
                tmp.append(k)
        for k in jqk:
            if k == "J":
                tmp.append(k)
        i = tmp + num
        result.append(i)

    return result


test_data = [["2", "K", "6", "A", "10", "Q","A"],
             ["8", "K"], ["9", "Q", "8", "A"], ["7"]]

result = sort_cards_bad(test_data)
print(result)
