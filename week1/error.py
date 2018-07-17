def div(dividend, divisor):
    try:
        print("The answer is %2.2f" % (dividend/divisor))
    except:
        pass


for i in range(5, -1, -1):
    for j in range(5, -1, -1):
        div(i, j)

def div2(a, b):
    if b == 0:
        raise ValueError("divisor cannot be zero!")
    else: return a/b

num = div2(1,0)
print(num)