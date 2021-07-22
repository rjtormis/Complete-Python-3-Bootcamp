def summer_69(arr):
    mylen = len(arr)
    add = True
    total = 0
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else: 
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    print(total)

summer_69([1, 3, 5])
summer_69([4, 5, 6, 7, 8, 9])
summer_69([2, 1, 6, 9, 11])