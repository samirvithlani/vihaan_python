choice = int(input(" enter choice \n press 1 for add \n press 2 for sub \n press 3 for mul \n press 4 for div"))
no1 = int(input("enter no 1"))
no2 = int(input("enter no 2"))
match choice:
    case 1:
        ans = no1 +no2
        print(f"ans = {ans}")
    case 2:
        ans = no1 - no2
        print(f"ans = {ans}")    
    
    case _:
        print("invalid choice..")    
        
