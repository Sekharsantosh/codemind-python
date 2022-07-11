n=input()
n=n.lower()
n=n.split()
a=["a","e","i","o","u"]
c=0
for i in n:
    if i[0] in a:
        if i[::-1] not in a:
           # print(i) 
            c=c+1
print(c)