def reverse(n):
    t=n
    rev=0
    while(t):
        r=t%10
        rev=rev*10+r
        t=t//10
    if rev==n:
        return True
    else:
        return False
n=int(input())
if(reverse(n)):
    print(True)
else:
    print(False)