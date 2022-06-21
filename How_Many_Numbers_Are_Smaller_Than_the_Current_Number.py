n=int(input())
c=0
b=[]
a=list(map(int,input().split()))
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[j]<a[i]:
           c=c+1
    b.append(c)
print(*b)