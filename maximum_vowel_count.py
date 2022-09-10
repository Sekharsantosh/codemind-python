n=input()
s="aeiou"
n=n.lower()
c=0
a=[]
for i in n.split():
    c=0
    for j in i:
        if j in s:
            c=c+1
    a.append(c)
print(max(a))