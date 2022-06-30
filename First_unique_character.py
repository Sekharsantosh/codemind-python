n=input()
n=n.lower()
n=n.split()
n="".join(n)
c=0
for i in n:
    if n.count(i)==1:
        c=i
        break
if c==0:
    print(-1)
else:
    print(c)