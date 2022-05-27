n=int(input())
a=list(map(int,input().split()))
k=0
s=set(a)
for i in s:
   if i%2!=0:
       k=k+1
print(k)