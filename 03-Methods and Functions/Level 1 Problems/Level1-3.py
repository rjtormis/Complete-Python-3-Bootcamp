#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(a):
    if abs(100-a) <= 10 or abs(200-a)<=10:
        print("True")
    else:
        print("False")
    return ((abs(100-a))<=10) or (abs(200-a)<=10)

almost_there(90)
almost_there(104)
almost_there(150)
almost_there(209)