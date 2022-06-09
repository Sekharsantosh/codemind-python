n,m=map(int,input().split())
b=[]
c=0
a=list(map(int,input().split()))
for i in range(len(a)+1):
    s=0
    for j in range(i,len(a)):
        s=s+a[j]
        if s==m:
            c=c+1
print(c)
    