def test():
    print("test function callled...")

test()    


def greet(name):
    print(f"Hello {name}")


#greet("Raj")    
#greet()

def add(a,b):
    return a + b

x = add(10,20)
print(f"ans = {x}")
print(f"ans = {add(100,200)}")

def avg(no1,no2)->int:
    return no1+no2

print(f"avg = {avg(10,20)}")
print(f"avg = {avg("ram "," sharma")}")


def isActive():
    return True

if isActive:
    print("if...")
else:
    print("else...")    
    
    
# crate a funciton whoch accessp a lisy as param and if all params are numbere add 10% profit to it and return nee list
# use comprehension    