n=input()
n=n.split()
n="".join(n)
s=min(n)
k=max(n)
c=0
v=0
for i in n:
    if i==s:
        c=c+1
    elif i==k:
        v=v+1
print(s,c,end=" ")
print(k,v,end=" ")