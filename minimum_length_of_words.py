n=input()
a=[]
for i in n.split():
    a.append(len(i))
print(min(a))