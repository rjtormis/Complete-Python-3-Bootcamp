#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
def count_primes(n):
   total = 0
   for num in range(2,n):
       Prime = True
       for i in range(2,num):
           if num % i == 0:
               Prime = False
       if Prime:
           total +=1
   print(total)

count_primes(100)
