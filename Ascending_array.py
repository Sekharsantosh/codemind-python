n=int(input())
a=list(map(int,input().split()))
m=0
for i in range(n-1):
    if(a[i]<a[i+1]):
        m=1
    else:
        m=0
        break
if(m==1):
    print("yes")
elif(m==0):
    print("no")