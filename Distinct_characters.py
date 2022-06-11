n=input()
n=n.split()
n="".join(n)
n=n.lower()
a=[]
n=set(n)
n=sorted(n)
for i in n:
    print(i,end="")