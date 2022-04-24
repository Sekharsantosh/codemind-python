n=int(input())
e=n
rev=0
while e:
    r=e%10
    rev=rev*10+r
    e=e//10
if(rev==n):
    print("True")
else:
    print("False")