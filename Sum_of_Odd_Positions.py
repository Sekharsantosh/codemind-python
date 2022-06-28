n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in range(len(a)):
    if i%2!=0:
        c=c+a[i]
print(c)