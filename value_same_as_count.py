n=int(input())
c=[]
x=list(map(int,input().split()))
for i in x:
     if i==x.count(i):
         c.append(i)
c=set(c)
k=0
for i in c:
   k+=1
print(k)