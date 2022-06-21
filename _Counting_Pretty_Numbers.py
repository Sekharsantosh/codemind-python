n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=0
    for i in range(a,b+1):
        if i<=10 and (i==2 or i==3 or i==9):
            c=c+1
        elif i>10:
            r=i%10
            if r==2 or r==3 or r==9:
                c=c+1
    print(c)