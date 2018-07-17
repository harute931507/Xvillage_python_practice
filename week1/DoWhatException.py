import random


class HungryException(Exception):
    def __init__(self, condition):
        self.condition = condition

    def __str__(self):
        return "I am humgry (status : " + str(self.condition) + "), need to eat !"


class ThirstyException(Exception):
    def __init__(self, condition):
        self.condition = condition

    def __str__(self):
        return "I am Thirsty (status : " + str(self.condition) + "), need to drink !"


class BoredException(Exception):
    def __init__(self, condition):
        self.condition = condition

    def __str__(self):
        return "I am Bored (status : " + str(self.condition) + "), need to play !"


def check(man):
    if man["water"] <= 0:
        raise ThirstyException(man["water"])
    elif man["hunger"] <= 0:
        raise HungryException(man["hunger"])
    elif man["mood"] <= 0:
        raise BoredException(man["mood"])


def play(man):
    print("playing...")
    man["hunger"] -= 15
    man["water"] -= 15
    man["mood"] += 5
    check(man)


def eat(man):
    print("eating...")
    man["hunger"] += 5
    check(man)


def drink(man):
    print("drinking...")
    man["water"] += 5
    check(man)


actionList = [play, eat, drink]

child = {"hunger": 20, "water": 20, "mood": 20}

while True:
    #cnt -= 1
    rand = random.randint(0, 2)

    try:
        actionList[rand](child)
    except HungryException as e:
        print(e)
        print("eating...")
        break
    except ThirstyException as e:      
        print(e)  
        print("drinking...")
        break
    except BoredException as e:   
        print(e)     
        print("playing...")
        break
