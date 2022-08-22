def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
for i in range(n):
    a=int(input())
    b=a
    c=a
    while True:
        if is_prime(b):
            break
        b=b+1
    while c !=0:
        if is_prime(c):
            break
        c-=1
    # print(a,b,c)
    if b-a==a-c:
        print(c)
    elif (b-a)<(a-c):
        print(b)
    else:
        print(c)
    