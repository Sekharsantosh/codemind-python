n,m=map(int,input().split())
a=list(map(int,input().split()))
k=0
#print(*a)
for i in a:
    if i%m==0:
        k=k+1
print(k)
    
