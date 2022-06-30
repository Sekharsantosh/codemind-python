n=int(input())
a=list(map(int,input().split()))
c=0
a=set(a)
for i in a:
        c=c+i
print(c)