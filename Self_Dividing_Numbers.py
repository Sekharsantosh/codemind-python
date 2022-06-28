def div(n):
    s=n
    c=0
    while(s):
        r=s%10
        if r!=0:
            if n%r==0 :
                c=c+1
        s=s//10
    n=str(n)
    if len(n)==c:
        return True
    else:
        return False
n=int(input())
m=int(input())
for i in range(n,m+1):
    if div(i):
        print(i,end=" ")