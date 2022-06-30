n=input()
m=input()
n=n.lower()
m=m.lower()
m=m.split()
n=n.split()
m="".join(m)
n="".join(n)
n=sorted(set(n))
m=sorted(set(m))
l=[]
for i in n:
    if i not in m:
        l.append(i)
for i in m:
    if i not in n:
         l.append(i)
l=sorted(l)
for i in l:
    print(i,end="")
