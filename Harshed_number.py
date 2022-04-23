n=int(input())
rev=0
e=n
while e:
    r=e%10
    rev=rev+r
    e=e//10
if n%rev==0:
    print("True")
else:
    print("False")