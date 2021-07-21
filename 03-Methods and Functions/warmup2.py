#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(a):
    mystring = a.split()
    if mystring[0][0] == mystring[1][0]:
        print("Both begin with the same letter")
        return True
    else:
        print("Two words did not begin with the same letter")
        return False


animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')