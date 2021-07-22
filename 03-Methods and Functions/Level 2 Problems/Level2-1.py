#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(a):
    mylen = len(a)
    for x in range(mylen-1):
        if a[x] == 3 and a[x+1] == 3:
            return print('True')
    return print('False')
            
            

has_33([1, 3, 3])
has_33([1, 3, 1, 3])           
has_33([3, 1, 3])
