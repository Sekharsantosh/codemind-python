n=int(input())
a=list(map(int,input().split()))
s,p=map(int,input().split())
b=[]
c=0
k=0
for i in a:
    if i not in range(s,p+1):
        b.append(i)
        c=c+1
if c==0:
    print("-1")
else:
    print(min(b))
    
    