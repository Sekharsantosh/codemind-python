def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
         if n%i==0:
             return False
    return True
def reverse(n):
    rev=0
    while(n):
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
k=0
j=0
if is_prime(n):
    k=1
    if k==1:
        n=reverse(n)
        if is_prime(n):
             j=1
if k==1 and j==1:
    print("circular prime")
elif k==1 and j!=1:
    print("prime but not a circular prime")
else:
    print("not prime")
    
    