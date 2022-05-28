n=int(input())
a=list(map(int,input().split()))
for i in a:
       if i<0:
           i=i*(-1)
       else:
           i=i*1
       k=len(str(i))
       print(k,end=" ")