n=input()
p=input()
n=n.lower()
p=p.lower()
c=0
for i in n.split():
    if i in p.split():
        c=c+1
print(c)
