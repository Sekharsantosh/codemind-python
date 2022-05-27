n=int(input())
c=0
a=list(map(int,input().split()))
k=set(a)
for i in k:
    #print(i)
    if(i>=0 and i<=1):
        c=1
    elif(i>1):
        c=0
        break
if c==1:
    print(True)
else:
    print(False)