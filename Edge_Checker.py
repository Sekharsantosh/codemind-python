n,p=map(int,input().split())
if n-p==1 or p-n==1 or n==10 and p==1 or n==1 and p==10:
    print("Yes")
else:
    print("No")