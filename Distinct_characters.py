n=input()
n=n.lower()
n=n.split()
n="".join(n)
n=sorted(n)
for i in n:
    if n.count(i)==1:
        print(i,end="")