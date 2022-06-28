n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,n+1):
       # print(i,end=" ")
        if  i not in a:
           print(i,end=" ")
           break