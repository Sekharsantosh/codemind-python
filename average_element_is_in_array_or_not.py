n=int(input())
a=list(map(int,input().split()))
m=0
c=0
#print(*a)
for i in a:
    m=m+i
k=m//len(a)
for i in a:
    if i==k:
        c=1
if c==1:
  print("True")
else:
   print(False)