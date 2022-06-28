n=int(input())
a=[]
c=0
while(n):
    r=n%10
    a.append(r)
    n=n//10
for i in a:
    if a.count(i)==1:
        c=1
    else:
        c=0
        break
if c==1:
    print("Unique Number")
else:
    print("Not Unique Number")