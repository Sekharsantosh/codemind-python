def digit(n):
    s=1
    if n>1:
        for i in range(1,n):
            s=s+s*i
    return s
n=int(input())
a=[]
k=0
e=n
while e:
    r=e%10
    a.append(r)
    e=e//10
#print(*a)
for i in a:
    k=k+digit(i)
if k==n:
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")
    