n=input()
s="aeiou"
n=n.lower()
c=0
for i in n.split():
    c=0
    for j in i:
        if j in s:
            c=c+1
    print(c,end=" ")