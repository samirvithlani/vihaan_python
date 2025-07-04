#it pure python functiun which will take other function as argument, adn will have inner function and return inner object
#use of decorator is to modify behaviour of function without changing code


def order_food(func): #func == throwParty
    
    def inner():
        print("ordering food")
        func() #throw_party()
    
    return inner    



@order_food #decorator
def throw_party():
    print("throwing party...")


throw_party()    