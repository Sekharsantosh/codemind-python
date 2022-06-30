n=input()
n=n.lower()
n=n.split()
n="".join(n)
n=set(n)
n=sorted(n)
for i in n:
        print(i,end="")