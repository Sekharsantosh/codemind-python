n=input()
p=input()
n=n.lower()
p=p.lower()
c=0
for i in n:
    if i in p:
        c=1
    else:
        c=0
        break
if c==1:
    print(True)
else:
    print(False)
