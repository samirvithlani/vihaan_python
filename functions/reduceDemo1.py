
import functools

marks = [1,2,3,4,5]

#1 2 -3
#3 3 =6
#6 4 =10
total = functools.reduce(lambda x,y:x+y,marks)
print(total)

