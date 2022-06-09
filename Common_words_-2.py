n=input()
p=input()
c=0
n=n.lower()
p=p.lower()
for i in n.split():
    for j in p.split():
        if n.count(i)==1 and p.count(i)==1 and i==j:
         
             c=c+1
print(c)

