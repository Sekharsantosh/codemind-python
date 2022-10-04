def deci(a):
    s=0
    i=0
    while a:
        r=a%10
        s=s+r*(2**i)
        a=a//10
        i+=1
    return s
def octal(a):
    k=""
    a=deci(a)
    while a:
        r=a%8
        k=k+str(r)
        a=a//8
    k=k[::-1]
    print(k)

n=int(input())
for i in range(n):
    a=int(input())
    octal(a)