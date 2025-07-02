#map -> []

marks = [10,11,22,21,20]

#x = map(function,object)
#marks1 = map(lambda x:x+5,marks)
marks1 = map(lambda x:x>10,marks)
print(list(marks1))

users = ["ram","amit","shyam","sundar","daya"]

upperuser = map(lambda x: x.upper(),users)
print(list(upperuser))

nested_list = [[1,2],[3,4],[5,6]]

ans = map(lambda i: list(map(lambda x:x*2,i)),nested_list)
print(list(ans))

ans = [list(map(lambda x:x*2,i)) for i in nested_list]
print(ans)




