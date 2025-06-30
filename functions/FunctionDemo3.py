#default argument function

def add(a=0,b=0,c=0):
    return a + b+ c

print(f"{add()}")
print(f"{add(10)}")
print(f"{add(10,20,30)}")


#named param function

# def getUserData(name,age,salary):
#     print(f"name = {name}")
#     print(f"age = {age}")
#     print(f"salary = {salary}")



# #getUserData(23,90000,"raj")
# getUserData(age=23,salary=90000,name="ram")
def getUserData(*,name,age,salary):
    print(f"name = {name}")
    print(f"age = {age}")
    print(f"salary = {salary}")



#getUserData(23,90000,"raj")
#getUserData(age=23,salary=90000,"ram") #left side...
#getUserData("ram",salary=90000,age=23) #left side...
#getUserData("ram",salary=90000,age=23) #left side...
getUserData(age=23,salary=90000,name="ram")











