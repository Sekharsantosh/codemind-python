n=int(input())
s=n*n
rev=0
while (n):
    r=n%10
    rev=rev*10+r
    n=n//10
k=rev*rev
tev=0
while(k):
    h=k%10
    tev=tev*10+h
    k=k//10

if(tev!=s):
    print("False")
else:
    print("True")