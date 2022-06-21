a=list(map(int,input().split(",")))
c=0
b=[]
for i in a:
    s=0
    for j in range(1,i+1):
        if i%j==0:
            s=s+j
    if s in a:
        b.append(i)
if len(b)==0:
    print(-1)
else:
    b=sorted(b)
    for i in b:
        print(i,end=" ")