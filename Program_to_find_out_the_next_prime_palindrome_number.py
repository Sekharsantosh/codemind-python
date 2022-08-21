def is_palindrome(n):
    rev=0
    t=n
    while(t):
        r=t%10
        rev=rev*10+r
        t=t//10
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
if n>0:
   n=n+1
while(n):
    t=is_palindrome(n)
    k=is_prime(n)
    if t==n and k==True :
            print(n)
            break
    elif t!=n or(k!=True):
       n=n+1







        
