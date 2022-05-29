m=int(input())
a=list(map(int,input().split()))
#print(*a)
j=sorted(a)
s=0
v=0
for i in j:
      if a.count(i)==1:
           s=i
if s>0:
    print(s)
else:
    print("-1")
           
      


    