#Problem 3
#Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def Errors():
    while True:
        try:
            result = int(input("Input an integer:"))
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            print(f'Thank you, your number squared is: {result **2}')
            break
Errors()