n=int(input())
c=0
a=list(map(int,input().split()))
for i in a:
    if i%2==0:
        c=i

print(c)