n=input()
p=input()
n=n.split()
n="".join(n)
n=n.lower()
p=p.split()
p="".join(p)
p=p.lower()
c=0

n=set(n)
p=set(p)
for i in n:
    if i in p:
        c=c+1
print(c)