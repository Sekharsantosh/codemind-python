n=int(input())
m=list(map(int,input().split()))
c=0
e=0
for i in m:
    if(i%2==0):
        c=c+1
    else:
        e=e+1
print(c,e ,end=" ")