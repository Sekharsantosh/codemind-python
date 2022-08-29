n=int(input())
a=list(map(int,input().split()))
s=0
k=len(a)
for i in a:
    s=s+(2**(k-1))*i
    k-=1
print(s)