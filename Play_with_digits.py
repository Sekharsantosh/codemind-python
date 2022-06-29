def reverse(n):
    t=n
    rev=0
    while(t):
        r=t%10
        rev=rev+r
        t=t//10
    return rev
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
      c=c+reverse(i)
print(c)
