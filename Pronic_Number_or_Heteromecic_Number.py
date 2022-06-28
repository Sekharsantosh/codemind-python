n=int(input())
c=0
k=0
for i in range(1,n//2):
    if n%i==0:
        c=i
    if c*(c-1)==n:
        k=1
if k==1:
    print("YES")
else:
    print("NO")
