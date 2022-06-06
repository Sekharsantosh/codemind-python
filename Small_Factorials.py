def fact(n):
    f=1
    for i in range(1,n):
        f=f+f*i
    return f
m=int(input())
a=[]
for i in range(m):
    v=int(input())
    a.append(v)
for i in a:
    print(fact(i))