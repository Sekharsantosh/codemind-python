n,m=map(int,input().split())
t=10**m
d=n%t
while(n>10**m):
    n=n//10
r=n;
print(abs(d-r))