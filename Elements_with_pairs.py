n=int(input())
a=list(map(int,input().split()))
s=len(a)
if s%2!=0:
    a.append(0)
print(*a)