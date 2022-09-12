n=int(input())
c=0
a=list(map(int,input().split()))
for i in range(1,n-1):
       if(a[i-1]%2==0 and a[i+1]%2==0):
            if a[i]%2!=0:
                 c=c+1
print(c)