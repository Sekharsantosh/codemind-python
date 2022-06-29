def reverse(n):
    t=n
    rev=0
    while(t):
        r=t%10
        rev=rev*10+r
        t=t//10
    if n==rev:
           return True
    else:
        return False
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if(reverse(i)):
        c=c+1
print(c)
