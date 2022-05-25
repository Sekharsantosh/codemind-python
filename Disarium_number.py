n=int(input())
a=[]
s=0
t=n
while t:
    r=t%10
    a.append(r)
    t=t//10
k=len(a)
h=k
for i in a:
    s=s+i**h
    h-=1
if s==n:
    print("True")
else:
    print("False")