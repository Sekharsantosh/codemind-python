def fibonacci(n):
    c=0
    f1=0
    f2=1
    a=[]
    while c<=n:
        f3=f1+f2
        f1=f2
        f2=f3
        c+=1
        a.append(f1)
    return a
n=int(input())
f=fibonacci(n)
k=0
s=0
for i in f:
    if i<n:
        k=i
    elif i>n:
        s=i
        break
if n-k<s-n:
    print(k)
elif n-k>s-n:
    print(s)
elif n-k==s-n:
    print(k,s)