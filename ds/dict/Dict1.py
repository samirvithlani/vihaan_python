users = {"id":1,"name":"ram","age":23,"status":True}
print(users)

keys = users.keys() #keys object of list
print(list(keys))

values = users.values()
print(list(values))

kv = users.items()
print(kv)

print("age",users["age"])  #error
print(users.get("status")) #None


# #iterable
# for k,v in users.items():
#     print(f"key = {k} value ={v}")

# for i in kv:
#     for j in i:
#         print(j)