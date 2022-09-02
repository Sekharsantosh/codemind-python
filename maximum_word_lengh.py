n=input()
#print(n)
a=[]
for i in n.split():
   # print(len(i))
    a.append(len(i))
print(max(a))