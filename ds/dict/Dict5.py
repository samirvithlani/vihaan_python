score = {"Virat":[90,78,56,12,78],"Hardik":[23,45,67,0,77],"Rohit":[87,67,0,15,23]}
score["sachin"]= [100,20,123,45,67]
#{virat:total,hardik,total}
finalScore={}
sum=0
for i,j in score.items(): #tuple("virat",[,,,,])
    for runs in j:
        #print(runs)
        sum = sum+runs
        finalScore[i]=sum
    sum=0


print(finalScore)        