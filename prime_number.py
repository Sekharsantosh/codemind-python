n=int(input())
for i in range (2,n):
    if n%i==0:
        c=1
        break
    else:
        c=0
if c==0:
    print("prime")
else:
    print("not a prime")
        