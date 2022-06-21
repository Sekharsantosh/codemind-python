n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
for i in a:
    if k==i:
        print(a.index(i))
        break
for i in a:
    if k not in a:
        print("-1")
        break