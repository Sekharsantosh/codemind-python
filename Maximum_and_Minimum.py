n=int(input())
Min=0
Max=0
a=list(map(int,input().split()))
for i in a:
    #print(i)
    if a.count(i)==i:
        Max=i
for i in a:
    if a.count(i)==i:
        Min=i
        break
    elif a.count!=i:
        Min=0
        Max=0
if Max>=1 and Min>=1:
    print(Min,Max)
else:
    print("-1")
