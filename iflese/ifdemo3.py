age = int(input("enter age :"))

if age >= 18:
    print("eligible for driving lic...")
    if age>=21:
        print("eligible for marrige...")
    else:
        print("not eligible for marrige ")
else:
    print("not eligible for driving lic...")
    if age>=16:
        print("eligible for 2 wheeler....")
    else:
        print("stay at home...")    