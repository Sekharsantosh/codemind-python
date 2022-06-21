n=int(input())
for i in range(n):
    e=int(input())
    a=list(map(int,input().split()))
    for i in range(1,e+1):
        if i not in a:
            print(i)