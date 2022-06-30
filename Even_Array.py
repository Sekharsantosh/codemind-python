n=int(input())
x=list(map(int,input().split()))
s=0
c=0
for i in x:
      if i%2==0:
         c=1
      else:
           c=0
           break
if c==1:
    print(True)
else:
    print(False)