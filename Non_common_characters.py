n=input()
p=input()
n=n.split()
n="".join(n)
n=n.lower()
p=p.split()
p="".join(p)
p=p.lower()
s=n+p
c=0
s=sorted(set(s))
for i in s:
    if i not in n:
        c=c+1
    elif i not in p:
         c=c+1
print(c)