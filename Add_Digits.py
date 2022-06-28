def summy(n):
    s=0
    while(n):
        r=n%10
        s=s+r
        n=n//10
    if s<=9:
        return s
    else:
        return summy(s)
n=int(input())
m=summy(n)
print(m)