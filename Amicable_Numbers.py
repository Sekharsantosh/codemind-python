n=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
p=int(input())
k=0
for a in range(1,p):
    if p%a==0:
        k=k+a
if s==p and k==n:
    print("Amicable")
else:
    print("Not Amicable")