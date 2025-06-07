data = {"Gujarat":"Gandhinagar","Maharashtra":"Mumbai","Up":"Lucknow"}
print(data)

data["Bihar"] = "Patna"
data["Gujarat"] = "Ahmedabad"

data.update({"Punjab":"Chandigadh","Maharashtra":"Bombey"})
print(data)
