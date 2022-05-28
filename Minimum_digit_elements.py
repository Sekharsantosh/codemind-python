n=int(input())
a=list(map(int,input().split()))
c=0
m=0
for i in a:
       '''print(i,end="  ")'''
       k=(len(str(i)))
       if k>m:
           m=k
for i in a:
    if len(str(i))<m:
        m=len(str(i))
for i in a:
    if m==len(str(i)):
        c=c+1
print(c)
# the end