n=int(input())
a=list(map(int,input().split()))
m,p=map(int,input().split())
b=[]
for i in range(n):
    if a[i] not  in range(m,p+1):
        b.append(a[i])
#print(*b)
if len(b)>0:
    print(min(b))
else:
    print(-1)