n,p=map(int,input().split())
gcd=0
for i in range(1,p):
    if(n%i==0 and p%i==0):
        gcd=i
print(gcd)