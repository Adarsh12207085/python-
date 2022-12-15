arr=[2,7,1,3,5,10,15,23,29,31,36,41]
print(list(filter(lambda x :x %2==0,arr)))
# second code for same output
# lambda is a anonymous function
list1=[]
for x in arr:
    if x%2==0:
        list1.append(x)
print(list1)