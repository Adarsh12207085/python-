flag=True
str=input()
len1=len(str)
start=0
end=len1-1
while start <end:
    if str[start]!=str[end]:
        flag=False
        break
    start+=1
    end-=1
if flag==True:
    print("palindrome")
else:
    print("not palindrome")
