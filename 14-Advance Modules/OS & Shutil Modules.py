f = open('practice.txt','w+')
f.write('This is a string')
f.close()

import os

print(os.getcwd())
print(os.listdir())
print(os.listdir('C:\\Users'))

import shutil

#shutil.move('practice.txt','C:\\Users\\tormis')

print(os.listdir('C:\\Users\\tormis'))