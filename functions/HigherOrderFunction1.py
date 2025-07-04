
def toBeCalled():
    print("to be called.........!!!")


def test(a):
    print(f"a = {a}")
    a()

# test(10)    
# test("ram")
# test(False)
# test([])    
test(toBeCalled)