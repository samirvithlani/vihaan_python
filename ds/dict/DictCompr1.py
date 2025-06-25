#{1:1,2:2,3:3,4:4,5:5}

# data = {i:i**2 for i in range(1,6)}
# print(data)


users = ["ram","amit","shyam","sundar","seeata"]
#{"ram":3}
# userWLen = {i:len(i) for i in users}
# print(userWLen)

userWLen = {i:len(i) for i in users if len(i)>3}
print(userWLen)


#users = ["ram","amit","shyam","sundar","seeata"]
#{'r':"ram","a":"amit"}

userwithini = {i[0]:i for i in users}
print(userwithini)


numers = [1,2,3,4,5,6,7,8,9,10]

numml = {i:"even" if i %2== 0 else "odd"  for i in numers}
print(numml)

#names =["amit","bob","naman","madam","shyam"]
#{"amit","Not","bob":"yes"}