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
    

