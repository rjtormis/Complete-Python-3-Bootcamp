#Use the iter() function to convert the string below into an iterator:
s = 'hello'
s_iter = iter(s)
for x in s_iter:
    print(x)
# Note both built - in function works the same as below but
# it would differ and depends on how the user / developer prefer to
# use the iter() func.
for y in s:
    print(y)