n=int(input())
e=n
k=e*e
c=0
t=10
while(e):
    r=k%t
    if(n==r):
        c=1
        break
    e=e//10
    t=t*10
if(c==1):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
