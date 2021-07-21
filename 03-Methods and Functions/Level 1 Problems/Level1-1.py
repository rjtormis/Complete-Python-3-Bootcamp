#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonalds(a):
    con = []
    for x in range(len(a)):
        if x == 0:
            con.append(a[x].upper())
        elif x == 3:
            con.append(a[x].upper())
        else:
            con.append(a[x])
    print(''.join(con))
    return ''.join(con)

old_macdonalds('macdonalds')