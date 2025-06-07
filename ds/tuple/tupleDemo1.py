data = ("ajay","raj")
print(data)
print(data[0])
#data[0] = "A"

print(data.index("raj"))
print(data.count("ajay"))

#aadhar car,pan,passport,     elction

data = ("ABCD123","PQR123","IND1121")
dataList = list(data)
dataList.append("ELEC1111")
data = tuple(dataList)
print(data)


players =[("Virat","RCB"),("MS","CSK"),("ROHIT","MI"),("KL","LSF")]
stats=[("Virat",741),("MS",200),("ROHIT",455),("KL",421)]


combined = [(p[0],p[1],s[1]) for p in players for s in stats if p[0]==s[0]]
#combine all pyaer info and stat ("playername","TEam",runs)
#list all player with runs>400
print(combined)

high_scorer = [(name,team,runs) for (name,team,runs) in combined if runs>400]
print(high_scorer)