# def demo():
#     print("demo ...")

# #print(demo)    
# x = demo
# #x == demo
# x()


x = lambda : print("demo called...")
x()

# def add(a,b):
#     print(a+b)

x1 = lambda a,b:print(a+b)
x1(100,20)

# def add(a,b):
#     return a+b

x2 = lambda a,b,c : a+b+c
print(x2(1,2,3))

findMax = lambda a,b: a if a>b else b
print(findMax(10,20))
findMax = lambda a,b,c: a if a>b else (b if b>c else c)
print(findMax(10,20,111))