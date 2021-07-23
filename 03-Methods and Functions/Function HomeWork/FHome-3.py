sample = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(s):
    HCase = 0
    LCase = 0
    for x in s:
        if x.isupper():
            HCase += 1
        elif x.islower():
            LCase += 1
    print(f'No. of Upper case characters :{HCase}')
    print(f'No. of Lower case characters :{LCase}')

up_low(sample)