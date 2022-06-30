n=int(input())
x=list(map(int,input().split()))
s=0
c=0
for i in x:
      s=s+i
k=s//len(x)
for i in x:
    if i>=k:
        c=c+1
print(c)