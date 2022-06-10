n=input()
m=input()
c=0
for i in n:
    if i in m:
        c=n.index(i)
if c>0:
    print("True")
    print(c)
else:
    print(False)