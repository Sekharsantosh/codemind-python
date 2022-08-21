def lcm(n,m):
    d=1
    if n>m:
        k=n
    else:
        k=m
    while True:
        if k%n==0 and k%m==0:
             return k
             break
        k=k+1
n,m=map(int,input().split())
print(lcm(n,m))
            
            
            
            
            