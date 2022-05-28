n=int(input())
a=list(map(int,input().split()))
s=0
b=[]
for i in a:
     #print(i,end=" ")
     if i not in b:
         b.append(i)
for i in b:
    if i%2!=0:
        s=s+i
print(s)
     
