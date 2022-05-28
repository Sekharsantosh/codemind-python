n,m=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
       if i<0:
           i=i*(-1)
       else:
           i=i*1
       k=len(str(i))
       if(k==m):
            c=c+1
print(c)