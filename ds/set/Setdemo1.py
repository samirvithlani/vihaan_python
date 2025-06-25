#{}
# data =set({})
# print(type(data))

data = {"raj","sahdev","virat","shrama","sahdev"}
print(data)

# print(data[0])

# for i in range(0,len(data)):
#     print(data[i])

# for i in data:
#     print(i)

data.add("ms")
data.update({"ajay","jadeja"})
print(data)


#remove...
removedelm= data.pop()
print(f"removing...{removedelm}")
print(data)

data.remove("jadejaa")
data.discard("jadeja")
print(data)