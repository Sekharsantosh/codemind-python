n=int(input())
t=0
a=1
while(n):
    r=n%10
    t=t+r
    a=a*r
    n=n//10
if t==a:
    print("Spy Number")
else:
    print("Not Spy Number")