n=int(input())
a=list(map(int,input().split()))
c=0
a=set(a)
for i in a:
    if  i%2==1:
              c+=i
print(c)