n=int(input())
t=n
if t<0:
 t=t*(-1)
rev=0
while t:
    r=t%10
    rev=rev*10+r
    t=t//10
if n<0:
    print(rev*(-1))
else:
    print(rev)