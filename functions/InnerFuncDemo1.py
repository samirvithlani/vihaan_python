# def outer():
#     print("ouyter function called...")
#     return 100


# # x = outer()
# # print(x)    

# x = outer
# print(x)
# ans = x()
# print("ans = ",ans)


# def outer():
#     print("outer...")
#     def inner():
#         print("inner....")
#         #return "inner........."
    
#     inner()

# outer()    
    


# def outer():
#     print("outer called..")
#     def inner():
#         print("inner called...")
#         return f"inner returning {1000}"
    
#     inr = inner() #call
#     print(f"inner return  = {inr}")
#     return f"outer returning...{2000}"

# x = outer()   
# print("x",x)

# def outer():
#     print("outer called..")
#     def inner():
#         print("inner called...")
#         return f"inner returning {1000}"
    
#     inr = inner() #call
#     print(f"inner return  = {inr}")
#     return f"outer returning...{inr}"

# x = outer()   
# print("x",x)



# def outer():
#     print("outer called..")
#     def inner():
#         print("inner called...")
#         return f"inner returning {1000}"
    
    
#     return inner() #call

# x = outer()   
# print("x",x)

# def outer():
#     print("outer called..")
#     def inner():
#         print("inner called...")
#         return f"inner returning {1000}"
    
    
#     return inner #pass

# x = outer()   
# print("x",x())
# # ans = x()
# # print("ans",ans)


def outer():
    print("outer called..")
    def inner(a):
        print("inner called...",a)
        return f"inner returning {1000}"
    
    
    return inner #pass

x = outer()   
print("x",x(90000))
# ans = x()
# print("ans",ans)