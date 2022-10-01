n,m=map(int,input().split())
if (abs(n-m)==1) or (n==1 and m==10) or (m==1 and n==10):
    print("Yes")
else:
    print("No")