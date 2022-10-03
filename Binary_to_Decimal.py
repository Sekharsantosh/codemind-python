def  sting(n):
    s=0
    i=0
    while n:
        r=n%10
        s=s+2**i*r
        n=n//10
        i+=1
    return s
        
n=int(input())
for i in range(n):
    a=int(input())
    print(sting(a))
    