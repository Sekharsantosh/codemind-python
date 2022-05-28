n=int(input())
s=0
import math
a=list(map(int,input().split()))
for i in a:
   # print(i)
    k=int(math.sqrt(i))
    if i==k*k:
        s=s+i
print(s)