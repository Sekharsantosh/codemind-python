def reverse(n):
    t=n
    rev=0
    while t:
        r=t%10
        rev=rev*10+r
        t=t//10
    return rev
n=int(input())
b=[]
a=list(map(int,input().split()))
for i in a:
    i=reverse(i)
    b.append(i)
print(*b)