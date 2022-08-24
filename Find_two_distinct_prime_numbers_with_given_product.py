def is_prime(n):
   if n==1:
       return False
   for i in range(2,int(n**0.5)+1):
       if n%i==0:
           return False
   return True
n=int(input())
k=0
f=0
p=0
a=[]
for i in range(1,n//2):
    for j in range(2,n//2+1):
        if is_prime(i):
            if is_prime(j):
                if i*j==n:
                    k=1
                    f=i
                    p=j
                    a.append(i)
                    a.append(j)
                    break
a=set(sorted(a))
if k==0:
    print(-1)
else:
    print(*a)