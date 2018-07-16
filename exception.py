class MyException(Exception):
    def __init__(self, err_msg):
        self.msg = err_msg

    def __str__(self):
        return "abc" + self.msg


class RelationException(Exception):
    def __init__(self, P1, P2):
        self.p1 = P1
        self.p2 = P2

    def __str__(self):
        return "Are you sure that " + self.p1 + " and " + self.p2 + " are in love with each other"


try:
    raise MyException("I'm an exception message!")
except MyException as e:
    print("---encountered MyEception---")
    print(e)

try:
    raise RelationException("Dad","Mom")
except RelationException as e:
    print("---encountered RelationEception---")
    print(e)
