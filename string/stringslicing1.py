name = "ahmedabad"
x = name[::]
print(x)
x = name[1::1]
print(x)
x = name[1:3:1]
print(x)
x = name[::-1]
print(x)


name = "naman"

if name == name[::-1]:
    print("name is palindrome")
else:
    print("name is not palindorme") 


no =121

if str(no) == str(no)[::-1]:
    print("yes")
    