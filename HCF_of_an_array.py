n=int(input())
a=list(map(int,input().split()))
m=a[0]
for i in range(len(a)):
    if m>a[i]:
        m=a[i]
for i in range(len(a)):
    if a[i]%m==0:
        c=1
    else:
        c=0
        break
if c==1:
    print(m)
else:
    print(1)