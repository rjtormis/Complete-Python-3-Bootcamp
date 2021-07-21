#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(a,b):
    if a == 20 or b == 20:
        print("Integer is 20")
        return True
    elif a + b == 20:
        print("Sum is 20")
        return True
    else:
        print("Incorrect")
        return False
makes_twenty(20,10)
makes_twenty(12,8)
makes_twenty(2,3)