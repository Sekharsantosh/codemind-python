n=int(input())
a=list(map(int,input().split()))
i=1
c=0
while i<len(a):
    if a[i]>a[i-1]:
        c=1
    i+=1
if c==1:
    print("no")
else:
    print("yes")