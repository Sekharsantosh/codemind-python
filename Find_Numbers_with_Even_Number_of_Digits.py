def digit_count(n):
    c=0
    k=0
    while n:
        n=n//10
        c=c+1
    return c
m=int(input())
a=list(map(int,input().split()))
s=0
v=0
for i in a:
    v=digit_count(i)
    if v%2==0:
        s=s+1
print(s)
    