import timeit

my_code = "a = 2+ 2"

print (timeit.timeit(stmt = my_code, number = 100001000))