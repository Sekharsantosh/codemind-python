n=input()
n=n.split()
n="".join(n)
n=n.lower()
c=0
for i in n:
    if n.count(i)==1 and i.isalpha():
        print(i,end="")
        c=1
        break
if c==0:
    print(-1)