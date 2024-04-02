#mission no. 2

#tbh I have no idea what you want so...
list2= []

def solve_puzzles(puzzles):

    if 'None' or 'False' or '0' in puzzles:
        list2.append('False')
    elif 'True' in puzzles:
        list2.append('True')
    elif float(puzzles) == True and not 0:
        list2.append('True')
    elif '[' and ']' in puzzles and list(puzzles)==True:
        if len(puzzles)==0:
            list2.append('False')
        else:
            list2.append('True')
    elif int(puzzles)== True and not 0:
        list2.append(puzzles)
    elif '{' and '}' and dict(puzzles)== True in puzzles:
        if len(dict(puzzles))==0:
            list2.append('False')
        else:
            list2.append('True')
    elif float(puzzles[1:-1]) == True and not 0:
        list2.append('True')
    elif list(puzzles[1:-1]) == True:
        if len(list(puzzles[1:-1])) ==0:
            list2.append('False')
        else:
            list2.append('True')
    elif dict(puzzles[1:-1]) == True:
        if len(dict(puzzles[1:-1])) ==0:
            list2.append('False')
        else:
            list2.append('True')
    else:
        list2.append('False')
    


# I didn't know to work with dictionaries
    
print("Please enter the values from puzzles.txt one by one")   
for i in range(49):
    solve_puzzles(input())

print(list2)
