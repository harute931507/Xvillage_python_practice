import operator as op
import timeit

def caesar_cipher1(words, shift):
    result = ""
    
    plainToAscii = [(ord(x) + shift - 97) % 26 for x in words]
    
    for y in plainToAscii:
        result += chr(y+97)

    return result

def caesar_cipher2(words, bias):
    
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    caesar = op.itemgetter(*[(alphabets.index(i)+ bias)% len(alphabets) for i in words])
    
    return "".join(list(caesar(alphabets)))

shift = 29

print(caesar_cipher1("xvillage", shift))
print(caesar_cipher2("xvillage", shift))

#t1 = timeit.timeit('caesar_cipher1("xvillage", 4)', 'from __main__ import caesar_cipher1', number=10000)
#t2 = timeit.timeit('caesar_cipher2("xvillage", 4)', 'from __main__ import caesar_cipher2', number=10000)

#print(t1)
#print(t2)