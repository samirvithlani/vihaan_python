# def getUsers(a):
#     print(a)


# getUsers(10)    

def getUsers(*args):
    print(args)


getUsers()    
getUsers(10)
getUsers(10,20)    
getUsers(10,20,90)    


def getUsers1(y,*args):
    print(args,y)
    

getUsers1(10,20,30)    


def getUsers2(*args,x):
    print(args,x)

getUsers2(10,20,30,40,x=100)    

