n=input()
s=n.split()
c=0
v=set("aeiou")
for i in n:
    if i in v:
        v.remove(i)
if len(v)==0:       
        print(True)
else:
        print(False)