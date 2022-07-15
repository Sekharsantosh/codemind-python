def count(n):
       c=0
       if n<0:
           n=-(n)
       while(n):
           c=c+1
           n=n//10
       return c
n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
#print(*a)
for i in a:
    b.append(count(i))
c=max(b)
m=[]
for i in a:
    if count(i)==c  and i not in m:
        m.append(i)
print(*m)
