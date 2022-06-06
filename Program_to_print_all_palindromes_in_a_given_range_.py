def palindrome(n):
    re=0
    t=n
    while(t):
        r=t%10
        re=re*10+r
        t=t//10
    if re==n:
        return True
    else:
        return False
n=int(input())
m=int(input())
for i in range(n,m+1):
    if(palindrome(i)):
        print(i,end=" ")