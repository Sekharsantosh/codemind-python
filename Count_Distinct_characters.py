n=input()
n=n.split()
n="".join(n)
n=n.lower()
c=0
n=set(n)
for i in n:
    if i.isalpha():
        c=c+1
print(c)