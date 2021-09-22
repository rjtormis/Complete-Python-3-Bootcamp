from collections import Counter


mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,]
mylist2 = ['a','a','a','b','b','b','c','c','c']
print(Counter(mylist))
print(Counter(mylist2))

from collections import defaultdict

d = {'a':10}
print(d)

from collections import namedtuple
Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(age=10,breed='Husky',name='Sam')
print(sammy.age)
