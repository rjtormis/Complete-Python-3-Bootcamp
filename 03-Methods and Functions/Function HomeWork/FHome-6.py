#Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(s):
    reverse = s[::-1]
    if reverse == s:
        print('Palindrome')
    else:
        print('Not palindrome')
    
palindrome('helleh')