n=int(input())
t=n
b=[]
s=0
while(t):
    r=t%10
    b.append(r)
    t=t//10
k=len(b)
for i in b:
    if k!=0:
       s=s+i**k
       k-=1
if s==n:
    print(True)
else:
    print(False)