n=int(input())
a=list(map(int,input().split()))
a.sort()
k=a[0]
c=0
t=0
for i in range(1,len(a)):
      if(a[i]>k):
             k=a[i]

c=a[0]
for i in range(0,len(a)):
      if a[i]>c and a[i]<k:
           c=a[i]
t=a[0]
for i in range(0,len(a)):
      if a[i]>t and a[i]<k and a[i]<c:
          t=a[i]
if(len(a)<3):
    print(max(a))
else:
    print(t)
