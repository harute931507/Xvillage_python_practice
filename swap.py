
a = 5
b = 6
print("Init")
print("a at", id(a), "is", a)
print("b at", id(b), "is", b)

a = a ^ b
b = a ^ b
a = a ^ b

print("Done")
print("a at", id(a), "is", a)
print("b at", id(b), "is", b)
