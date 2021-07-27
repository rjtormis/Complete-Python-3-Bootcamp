#Problem 1
#Handle the exception thrown by the code below by using try and except blocks.

def Errors():
    try:
        for i in ['a','b','c']:
            print(i**2)
    except:
        print("An Error Occured!")

Errors()