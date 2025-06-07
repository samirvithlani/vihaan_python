numbers = [0,1,2,3,4,5,0,6,7,8,9,10]

#x = ["even" if i %2 ==0 else "odd" for  i in numbers]
x = ["even" if i %2 ==0 else ("zero" if i == 0 else "odd") for  i in numbers]
print(x)

#chrome history
#day vise
#
#find most visted site
#find least visted site
#and dispaly all sites