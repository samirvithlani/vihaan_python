def add(*args):
    print(args)
    finalList =[]
    for i in args:
        for j in i:
            finalList.append(j)
    sum = 0
    for i in finalList:
        if i not in args[0] or i not in args[1]:
            sum = sum + i
    
    return sum        
            
        
    


x = add([1,2,3],[2,3,4])
print(x)
    