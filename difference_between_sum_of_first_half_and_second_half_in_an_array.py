n=int(input())
a=n//2
s=0
c=0
x=list(map(int,input().split()))
for i in range(n-1,a-1,-1):
     s=s+x[i]
for i in range(a):
    c=c+x[i]
print(abs(s-c))