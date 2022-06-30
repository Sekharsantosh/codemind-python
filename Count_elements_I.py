n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0#solved by santosh
a=set(a)
b=set(b)

for i in a:
     if i in b:
         c=c+1
print(c)