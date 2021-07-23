#Hard:
#Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
import string
def ispangram(str1,alphabet =string.ascii_lowercase):
    alphaset = set(alphabet)
    str1 = str1.replace(" ","")
    str1 = str1.lower()
    str1 = set(str1)
    if alphaset == str1:
        print('True')

ispangram("The quick brown fox jumps over the lazy dog")