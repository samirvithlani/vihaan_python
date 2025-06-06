#list compreh 
#[1,2,3,4,5,6,7,8,9,10]
#for i in range(1,11):
#   x.append(i)

x = [i for i in range(1,11)]
print(x)

data = [1,2,3,4,5,6,7,8,9,10]

x1=[i**2 for i in data]
# for i in data:
#     x1.append(i**2)

print(x1)   

sales = [100,200,300,400,500,600,700,800,900,1000] 

salesgt500 = [i for i in sales if i>500]

# for i in sales:
#     if i>500:
#         salesgt500.append(i)

print(salesgt500)        


users = ["ram","shyam","sumit","sam","sanjna","seeta"]

slist =[i for i in users if i.startswith("s")]
print(slist)


data =["ram","madam","naman","racecare","ajay","bob"]