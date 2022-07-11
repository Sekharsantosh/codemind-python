n=input()
c=1
for i in n:
    if n.count(i)==1:
        c=1
    else:
        c=0
        break
if c==1:
    print(True)
else:
    print(False)