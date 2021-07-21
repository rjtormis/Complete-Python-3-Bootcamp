# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 ==0:
        if a  > b:
            print(a)
            return a
        else:
            print(b)
            return b
    else:
        if a > b:
            print(a)
            return a 
        else:
            print(b)
            return b

lesser_of_two_evens(2,4)
lesser_of_two_evens(2,5)
    

