#Problem 1¶
#Create a generator that generates the squares of numbers up to some number N.

def gensquares(N):
    for x in range(N):
        yield x ** 2

for number in gensquares(10):
    print(number)