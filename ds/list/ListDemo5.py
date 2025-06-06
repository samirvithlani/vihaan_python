lang = ["java","python","js","php","c"]

# x = lang.index("python")
# print("x",x)

#lang.reverse()
#lang.sort(reverse=True)
#lang.sort(key=len,reverse=True)
print(lang)



#names = ["naman","raj","bob","racecar","ajay","madam"]

#rotate

k=3

mylist=[1,2,3,4,5]
##[4,5,1,2,3]
#[3,4,5,1,2]


rotated_list = mylist[-k:] + mylist[:-k]
print(rotated_list)

