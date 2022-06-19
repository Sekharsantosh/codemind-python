def palindrome(n):
    t=n
    rev=0
    while t:
        r=t%10
        rev=rev*10+r
        t=t//10
    if n==rev:
        return True
    else:
        return False
n=int(input())
c=0
a=list(map(int,input().split()))
for i in a:
    if palindrome(i):
        c=c+1
print(c)
