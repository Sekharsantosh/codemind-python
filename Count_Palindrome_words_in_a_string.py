n=input()
c=0
n=n.lower()
for i in n.split():
        if i==i[::-1]:
             c=c+1
print(c)