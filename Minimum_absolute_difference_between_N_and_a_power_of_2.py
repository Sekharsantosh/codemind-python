n=int(input())
#print(n)
k=0
z=0
for i in range(1,n//2+1):
    if(2**i>n):
        k=2**i
        break
for i in range(1,n//2+1):
    if (2**i<=n):
          z=2**i
#print(z,k)
#print(k-n)
if(z==n or k==n):
    print("0")
elif(k-n<n-z):
    print(k-n)
else:
    print(n-z)