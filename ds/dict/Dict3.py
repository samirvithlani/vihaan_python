data = {"Gujarat":"Gandhinagar","Maharashtra":"Mumbai","Up":"Lucknow"}

# removedValue = data.pop("Up")
# print(f"Remving...{removedValue}")
# print(data)

removedValue = data.popitem()
print(f"Remving...{removedValue}")
print(data)
