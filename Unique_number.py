n=int(input())
a=[]
b=[]
flag=0
while(n):
    r=n%10
    a.append(r)
    n=n//10
for i in a:
    if  a.count(i)>1:
        flag=1
if(flag!=1):
    print("Unique Number")
else:
    print("Not Unique Number")