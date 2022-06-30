n=int(input())
x=list(map(int,input().split()))
s=0
c=0
for i in x:
      if i==0 or i==1:
         c=1
      else:
           c=0
           break
if c==1:
    print(True)
else:
    print(False)