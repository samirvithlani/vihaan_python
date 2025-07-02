def getData():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5



# x = getData()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

for i in getData():
    print(i)