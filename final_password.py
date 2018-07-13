import random

Min = ""
Max = ""
while Min == "":
    Min = input("Enter the Lower Bound : ")
while Max == "":
    Max = input("Enter the Upper Bound : ")
Min = int(Min)
Max = int(Max)

answer = random.randint(Min, Max)
guess = answer+1

while guess != answer:
    guess = input("Enter your guess in range %d ~ %d : " % (Min, Max))
    if guess != "":
        guess = int(guess)
    else:
        continue

    if guess > answer:
        print("Too Big")
        if guess < Max:
            Max = guess
    elif guess < answer:
        print("Too Small")
        if guess > Min:
            Min = guess
    else:
        print("Correct!!")
