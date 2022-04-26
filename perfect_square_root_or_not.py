n=int(input())
import math
s=math.sqrt(n)
flag=0
for i in range(1,n//2):
    if(i==s):
        flag=1
        break
if(flag==1):
    print("True")
else:
    print("False")