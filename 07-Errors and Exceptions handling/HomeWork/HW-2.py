#Problem 2
#Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

def Errors():
    try:
        x = 5
        y = 0

        z = x/y
    except:
        print("An Error Occured!")
    finally:
        print('All Done!')

Errors()