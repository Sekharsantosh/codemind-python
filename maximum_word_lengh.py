n=input()
k=n.split()
for i in k:
    m=len(str(i))
for i in k:
    if len(str(i))>m:
        m=len(str(i))
print(m)