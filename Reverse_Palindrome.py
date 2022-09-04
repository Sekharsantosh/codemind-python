def reverse(n):
    rev=0
    t=n
    while(t):
        r=t%10
        rev=rev*10+r
        t=t//10
    return rev
def is_palindrome(n):
    rev=0
    t=n
    k=0
    while(t):
        r=t%10
        rev=rev*10+r
        t=t//10
    if n==rev:
        return True
    elif n!=rev:
        return False
        return is_palindrome(n+rev)
n=int(input())
k=n
s=0
while(True):
   if(is_palindrome(k+reverse(k))):
       print(k+reverse(k))
       break
   k+=reverse(k)
   

