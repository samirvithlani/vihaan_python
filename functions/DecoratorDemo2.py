
def order_food(func): #3 func == throw_party
    
    def inner(): #6
        print("ordering food...") #7
        func() #8
    
    return inner     #4


@order_food #2 #5
def throw_party(): #9
    print("Let's throw a party!") #10
    

throw_party()  #1    