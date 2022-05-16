n=list(map(int,input().split()))
p=list(map(int,input().split()))
c=0
k=0
a=[]
for i in range(3):
    if n[i]>p[i]:
        c=c+1
    elif n[i]<p[i]:
        k=k+1
    a=[c,k]
for i in a:
       print(i,end=" ")
