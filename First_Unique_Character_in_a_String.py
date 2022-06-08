n=input()
c=0
for i in n:
    if n.count(i)==1:
        c=n.index(i)
        break
    else:
        c=-1
print(c)