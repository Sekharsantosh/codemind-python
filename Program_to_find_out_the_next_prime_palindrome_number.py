def pal(n):
    rev=0
    t=n
    while t:
        r=t%10
        rev=rev*10+r
        t=t//10
    if n==rev:
        return True
    else:
        return False
def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
while True:
    n=n+1
    if pal(n):
        if is_prime(n):
            print(n)
            break
        