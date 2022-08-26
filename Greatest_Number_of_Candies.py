strength=int(input())
candies=list(map(int,input().split()))
extra_candy=int(input())
#print(candies)
k=max(candies)
#print(k)     an art by santosh...
a=[]
h=0
for i in candies:
    for j in range(1,extra_candy+1):
        if i+j>=k or i==k:
             h=1
        else:
            h=0
    if h==1:
             print(True,end=" ")
    else:
             print(False,end=" ")

    