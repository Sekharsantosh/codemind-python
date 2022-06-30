n=input()
p=input()
c=0
n=n.lower()
p=p.lower()
for i in n.split():
    if i in p.split():
         
             c=c+1
print(c)