def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def display(a):
    t=a
    k=0
    d=0
    f=0
    h=0
    while True:
        t=t+1
        if is_prime(t):
            k=t
            break
    while True:
        t=t-1
        if is_prime(t):
            d=t
            break
    f=abs(k-a)
    h=abs(a-d)
    if f<h:#47 51 53 
        print(k)
    elif f>h:
        print(d)
    else:
        print(d)
n=int(input())
for i in range(0,n):
    a=int(input())
    display(a)


        
