def amica(t):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    return s
n=int(input())
m=int(input())
#print(n,m)
p=amica(n)
k=amica(m)
#print(k,p)
if p==m or k==n:
    print("Amicable")
else:
    print("Not Amicable")