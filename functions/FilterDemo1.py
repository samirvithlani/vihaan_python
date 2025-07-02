users = ["raj","amit","kunal","sheetal","sneha","sam","shraddha","shruti"]

#sstart = filter(lambda x : x.startswith("s"),users)
sstart = filter(lambda x : x[0]=="s",users)
print(list(sstart))

lenfilt = filter(lambda x:len(x)>4,users)
print(list(lenfilt))