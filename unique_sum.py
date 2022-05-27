n=int(input())
a=list(map(int,input().split()))
k=0
s=set(a)
for i in s:
    k=k+i
print(k)