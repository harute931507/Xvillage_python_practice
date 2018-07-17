def isPrime(num):
    for i in range(2, round(num/2)+1):
        if num % i == 0:
            return False
    return True


Min = ""
Max = ""
while Min == "":
    Min = input("Enter the Lower Bound : ")
while Max == "":
    Max = input("Enter the Upper Bound : ")
Min = int(Min)
Max = int(Max)

for i in range(Min, Max):
    if isPrime(i) :
        if i >= 2:
            print(i, end=" ")
