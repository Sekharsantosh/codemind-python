n=input()
m=input()
n=n.lower()
m=m.lower()
m=m.split()
n=n.split()
for i in m:
    if i in n:
        print(i,end=" ")