user1 = {"ram","seeta"}
user2 = {"ram","seeta","arjun","sahdev"}

#x = user1.union(us
# er2)
#x = user1 | user2 #same as union
#x = user1.difference(user2)
#x = user1 - user2
#x = user1.intersection(user2)
#x = user1 & user2
#x = user1.symmetric_difference(user2)
x = user1.issubset(user2)
x = user1.issuperset(user2)
print(x)