n=input()
c=0
a=[]
v=set("aeiou")
for i in v:
    if i not in n:
         a.append(i)
         #print(i)
         c=1
    else:
        c=0
if c>0:
    a=sorted(a)
    print(*a)
else:
    print(0)