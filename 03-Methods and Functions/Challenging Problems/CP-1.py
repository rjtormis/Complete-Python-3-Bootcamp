#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(arr):
    spycheck = []

    for x in arr:
        if x == 0:
            spycheck.append(x)
        elif x == 7:
            spycheck.append(x)
    if spycheck[0] == 0 and spycheck[1] == 0:
        print('True')
    else:
        print('False')

    
        
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])