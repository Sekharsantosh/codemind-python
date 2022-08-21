n=int(input())
s=str(n)
k=len(s)
f=n*n
if (f%10**k==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")