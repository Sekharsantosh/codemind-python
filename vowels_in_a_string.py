n=input()
k=input()
l=0
a=0
for i in n:
    if k in n:
        l=1
        a=n.index(k)
if l==1:
    print("True")
    print(a)
else:
    print("False")
