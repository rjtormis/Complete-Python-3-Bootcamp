#MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(a):
    mystring = a.split()
    mystring.reverse()
    # Added modififaction
    # What if the input is more than 4 words
    print(' '.join(mystring))
        

    
master_yoda('I am home')
master_yoda('We are ready')