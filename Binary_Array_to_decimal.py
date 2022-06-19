n=int(input())
a=list(map(int,input().split()))
d=0
for i in a:
    d=d*2+int(i)
print(d)