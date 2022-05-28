n=int(input())
a=list(map(int,input().split()))
c=0
m=0
for i in a:
       k=len(str(i))
       if k>m:
           m=k
for i in a:
    if m==len(str(i)):
         c=c+1
print(c)