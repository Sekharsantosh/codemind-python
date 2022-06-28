n=int(input())
a=0
b=1
e=0
d=[]
for i in range(2,n):
    c=a+b
    a=b
    b=c
    d.append(c)
for i in d:
    if n in d:
        e=1
    else:
        e=0
if e==1:
    print("True")
else:
    print("False")