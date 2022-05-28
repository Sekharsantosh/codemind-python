n=int(input())
a=list(map(int,input().split()))
s=0
c=0
b=[]
for i in a:
    #print(i,end=" ")
    if a.count(i)==i and i not in b:
        b.append(i)
        c=c+1
#print(s,c)
print(c)
     
     
