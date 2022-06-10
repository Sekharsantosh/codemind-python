n=input()
p=input()
n=n.lower()
p=p.lower()
for i in p.split():
    if i in n.split():
        print(i,end=" ")
