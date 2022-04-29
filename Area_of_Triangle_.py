a,b,c=map(int,input().split())
s=(a+b+c)/2
import math
k=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("{:.2f}".format(k))