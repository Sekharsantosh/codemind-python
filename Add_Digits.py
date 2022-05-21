def sum_dig(n):
    s=0
    while(n):
        r=n%10
        a=n//10
        s=a+r
        if(s>9):
            n=s
            continue
        else:
           return s
n=int(input())
k=sum_dig(n)
print(k)