n=int(input())
#print(n)
f1=0
f2=1
f3=f1+f2
k=0
h=0
a=[]
for i in range(2,n+1):
        f1=f2
        f2=f3
        f3=f1+f2
        a.append(f1)
#print(*a)
for i in a:
    if i<n and i!=0:
        k=i
for i in a:
    if i>k :
        h=i
        break
#print(k,h)
if n-k <h-n:
    print(k)
elif n-k>h-n:
    print(h)
else:
    print(k,h)
