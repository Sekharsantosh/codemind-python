n = int(input())
a = list(map(int,input().split()))
for i in range(n-1):
    if a[i]<a[i+1]:
        k=0
        break
    else:
        k=1
if k==1:
    print("yes")
else:
    print("no")