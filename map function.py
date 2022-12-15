#higher order function ----- map function
str=["computer", "science", "student"]
print(list(map(lambda x:x.upper(),str)))
#both the code are same but down code is written
#  in four steps and upeer code is written in only 2 steps.
list1=[]
for x in str :
    list1.append(x.upper())
print(list1)