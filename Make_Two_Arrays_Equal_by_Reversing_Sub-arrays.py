a=int(input())
ar=list(map(int,input().split()))
b=int(input())
br=list(map(int,input().split()))
k=0
for i in ar:
    if i in br:
         k=1
    else:
        k=0
        break
if k==1:
    print("True")
else:
    print("False")