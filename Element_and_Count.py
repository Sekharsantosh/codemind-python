n=int(input())
a=list(map(int,input().split()))
s=0
b=[]
for i in a:
     k=a.count(i)
     if i not in b:
          b.append(i)
          print(i,a.count(i),end=" ")
     
