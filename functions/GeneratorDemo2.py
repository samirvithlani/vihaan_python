#10
#20
#500
def getData(batch,size):
    yield [i for i in range(1,11)]
    yield [i for i in range(11,21)]
    yield [i for i in range(21,31)]
    yield [i for i in range(31,41)]
    yield [i for i in range(41,51)]


for i in getData():
    print(i)    