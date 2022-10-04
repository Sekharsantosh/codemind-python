def binary(n):
    s=""
    while n:
        r=n%2
        s=s+str(r)
        n=n//2
    return s
def complement(n):
    n=binary(n)
    s=""
    for i in n:
        if i=="1":
            s=s+"0"
        elif i=="0":
            s=s+"1"
    s=s[::-1]
    k=0
    i=0
    s=int(s)
    while s:
        r=s%10
        k=k+r*2**i
        s=s//10
        i+=1
    print(k)
n=int(input())
complement(n)