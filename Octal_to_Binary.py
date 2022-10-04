def deci(a):
    s=0
    i=0
    while a:
        r=a%10
        s=s+r*8**i
        a=a//10
        i+=1
    return s
def octal(a):
    a=deci(a)
    k=""
    while a:
        r=a%2
        if r>=0:
           k=k+str(r)
        a=a//2
    k=k[::-1]
    print(k)

n=int(input())
for i in range(n):
    a=int(input())
    octal(a)