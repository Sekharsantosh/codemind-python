n=int(input())
a=list(map(int,input().split()))
m=0
c=0
#print(*a)
for i in a:
    m=m+i
k=m/len(a)
print("{:.2f}".format(k))