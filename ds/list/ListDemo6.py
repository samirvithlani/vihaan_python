data = [["virat",64],["sachin",35],["ms",45],["hardik",22]]

print(data)
print(data[0])
print(data[0][0])

# for i in data:
#     #print(i)
#     for j in i:
#         print(j,end=" ")
#     print()    

min =200
for i ,j in data:
    if j< min:
        min = j

print(min)        
    

