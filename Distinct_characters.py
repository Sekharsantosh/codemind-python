n=input()
n=n.split()
n="".join(n)
n=n.lower()
n=sorted(n)
for i in n:
    if n.count(i)==1:
        print(i,end="")