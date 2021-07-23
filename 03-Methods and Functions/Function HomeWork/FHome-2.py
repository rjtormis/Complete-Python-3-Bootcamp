#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    counter = False
    for x in range(low,high+1):
        if x == num:
            counter = True
    if counter == True:
        print(f'{num} is in the range between {low} and {high}')
    else:
        print(f'{num} is not in the range between {low} and {high}')

ran_check(5,2,7)