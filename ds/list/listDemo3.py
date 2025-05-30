sales =[100,200,222,456,789,909,161]
print(sales)
#sales.clear()
remvoedELm = sales.pop() #IndexError: pop from empty list
#remvoedELm = sales.pop(5)
print("removing...",remvoedELm)
print(sales)
# if 2222 in sales:
#     sales.remove(2222)

x = sales.count(222)
if x>0:
    sales.remove(222)
print(sales)