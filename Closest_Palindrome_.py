def pali(n):
    rev=0
    t=n
    while t:
        r=t%10
        rev=rev*10+r
        t=t//10
    if n==rev:
        return True
    else:
        return False
n=int(input())
k=0
l=0
t=n
while(t):
    t=t+1
    if pali(t):
        k=t
        break
f=n
while(f):
    f=f-1
    if pali(f):
        l=f
        break
d=abs(n-k)
h=abs(n-l)
if d<h:
    print(k)
elif d>h:
    print(l)
else:
    print(l,k)
