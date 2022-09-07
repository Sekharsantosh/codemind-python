n=int(input())
a=list(map(int,input().split()))
m=int(input())
for i in range(m):
    a.insert(0,a[-1])
    a.pop()
print(*a)