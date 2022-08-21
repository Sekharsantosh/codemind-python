def reverse(n):
    rev=0
    while(n):
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
k=reverse(n)
s=k*k
t=reverse(s)
if t==n*n:
    print(True)
else:
    print(False)