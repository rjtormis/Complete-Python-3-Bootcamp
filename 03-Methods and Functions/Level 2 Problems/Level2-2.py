#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(a):
    done = []
    for x in a:
        done.append(x*3)
    print(''.join(done))

paper_doll('Hello')
paper_doll('Mississippi')