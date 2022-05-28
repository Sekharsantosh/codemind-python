n=int(input())
a=list(map(int,input().split()))
s=int(input())
c=0
b=[]
for i in a:
    #print(i,end=" ")
    if a.count(i)==s and i not in b:
        b.append(i)
        c=c+1
#print(s,c)
if(c==0):
    print("-1")
else:
    print(*b)
     
     
