class relationError(Exception):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "Are you sure that " + self.p1 + " and " + self.p2 + " are in love with each other ?"


relation = {'Jason': 'Mary', 'Mary': 'Jason', 'Jennifer': 'Ken',
            'Ken': 'Jennifer', 'Tina': 'Kim', 'Kim': 'Tina'}


def check(pa, pb):
    try:
        if relation[pa] != pb:
            raise relationError(pa, pb)
    except KeyError:
        print("No relation found")
        raise relationError(pa, pb)


try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1, p2)
    print("{} and {} are in love with each other!".format(p1, p2))

except relationError as e:
    print(e)
