n=int(input())
a=list(map(int,input().split()))
c=0
#print(*a)
for i in reversed(range(len(a))):
    if a[i]%2==1:
        c=i
        break
print(c)