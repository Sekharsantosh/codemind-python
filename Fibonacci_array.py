n=int(input())
a=list(map(int,input().split()))
m=0
for i in range(2,n):
    if(a[i]==a[i-1]+a[i-2]):
        m=1
    else:
        m=0
        break
if(m==1):
    print("yes")
elif(m==0):
    print("no")