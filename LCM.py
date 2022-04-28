n,p=map(int,input().split())
gcd=0
if(p>n):
    for i in range(1,p+1):
        if n%i==0 and p%i==0:
            gcd=i
lcm=(n*p)//gcd
print(lcm)