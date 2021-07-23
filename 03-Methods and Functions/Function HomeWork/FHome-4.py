#Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(a):
    convert_set= set(a)
    convert_list = list(convert_set)
    print(f'Unique list is as follow : {convert_list}')

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])