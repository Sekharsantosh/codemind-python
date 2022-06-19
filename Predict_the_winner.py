n=int(input())
c=0
s=0
p=0
a=list(map(int,input().split()))
for i in a:
    su=min(a)
    s=s+su
    pu=max(a)
    p=p+pu
    a.remove(su)
    a.remove(pu)
k=abs(s-p)
if k%n==0:
    print("X")
else:
    print("Y")