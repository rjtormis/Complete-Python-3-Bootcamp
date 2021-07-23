#Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    pi = 3.1415926535897931
    r = rad
    v = 4.0/3.0*pi* r**3
    print(v)

vol(2)