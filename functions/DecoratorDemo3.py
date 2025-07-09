
def order_food(func):
    
    def inner(nopers):
        print(f"no of person = {nopers}")
        return func(nopers+100)
    
    return inner    
        

@order_food
def throw_party(no):
    print(f"let's throw party {no}")
    return "ok"


x = throw_party(100)    
print(x)