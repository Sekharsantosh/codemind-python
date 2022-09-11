n,m=map(int,input().split())
mat=[]

for i in range(n):
    r=list(map(int,input().split()))
    l=0
    for j in range(m):
        l=sum(r)
    print(l,end=" ")
       