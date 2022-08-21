def reverse(n):
    rev=0
    while(n):
       r=n%10
       rev=rev*10+r
       n=n//10
    return rev
def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
    return True
n=int(input())
k=0
f=reverse(n)
if is_prime(n):
    if is_prime(f):
           print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")






    








        
