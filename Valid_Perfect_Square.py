n=int(input())
import math
a=[]
for i in range(0,n):
    j=int(input())
    a.append(j)
for i in a:
    k=int(math.sqrt(i))
   # print(k)
    if i==k*k:
        print("True")
    else:
        print("False")