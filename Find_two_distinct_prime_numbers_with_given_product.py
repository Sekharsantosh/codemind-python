def is_prime(n):
    if n==1:
        return False
    elif n>1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
n=int(input())
k=0
a=[]
for i in range(1,n):
    if is_prime(i):
        a.append(i)
for i in a:
    for j in a:
        if i<j:
          if i!=j and (n%i==0 and n%j==0):
             k=1
             print(i,j)
             break
if k<=0:
    print(-1)