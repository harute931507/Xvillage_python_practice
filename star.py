level = ""
while level == "":
    level = input("Level is : ")
level = int(level)

level1 = level
level2 = level
while level1 > 0:
    while level2 > 0:
        print("*", end="")
        level2 -= 1
    level2 = level1-1
    level1 -= 1
    print('')

level3 = level
level4 = level
level5 = level
while level3 > 0:
    level5 = level - level4

    while level5 > 0:
        print(" ", end="")
        level5 -= 1

    while level4 > 0:
        print("*", end="")
        level4 -= 1
    level4 = level3-1
    level3 -= 1
    print('')
