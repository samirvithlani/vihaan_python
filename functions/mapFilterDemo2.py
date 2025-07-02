users = ["raj","amit","kunal","sheetal","sneha","sam"]

x = map(lambda i : i.upper(),filter(lambda x:x.startswith("s"),users))
print(list(x))
