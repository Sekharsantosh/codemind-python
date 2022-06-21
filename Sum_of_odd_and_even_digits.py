n=int(input())
a=list(map(int,input().split()))
c=0
k=0
for i in range(len(a)):
    if i%2==0:
        c=c+a[i]
    else:
        k=k+a[i]
if c-k==0 or k-c==0:
    print("YES")
else:
    print("NO")