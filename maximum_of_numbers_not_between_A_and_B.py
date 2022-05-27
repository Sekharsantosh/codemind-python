n=int(input())
a=list(map(int,input().split()))
m,p=map(int,input().split())
for i in a:
    if max(a) not in range(m,p+1):
          print(max(a))
          break
    else:
         print("-1")
         break