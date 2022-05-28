n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if i==0 :
        c=1
    elif i%2==0:
        c=1
       # print(i)
    elif i%2!=0 :
          c=0
          break
         # print(i)
if c==1:
   print(True)
else:
   print(False)