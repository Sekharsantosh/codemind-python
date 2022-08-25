def self_div(n):
   t=n
   k=0
   while t:
        k=0
        r=t%10
        if r>0 and n%r==0:
            k=1
        else:
            k=0
            break
        t=t//10
   if k==1:
       return True
   else:
       return False
n=int(input())
m=int(input())
for i in range(n,m+1):
       if self_div(i):
           print(i,end=" ")
    