students = [("Alice", 85), ("Bob", 92), ("Charlie", 85), ("David", 92), ("Eva", 78)]

result = {}

for name,grade in students:
    #Alice ,85
    #Chralie,85
    if grade in result:
        #resukt[85].append(charlie)
        result[grade].append(name)
    else:
        #result[85]=Alice
        result[grade]=[name]   
        
        
    

print(result)            