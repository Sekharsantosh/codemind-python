n=int(input())
c=0
a=list(map(int,input().split()))
m,p=map(int,input().split())
for i in a:
    if i not in range(m,p+1):
          c=c+i
print(c)