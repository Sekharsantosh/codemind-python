t=int(input())
for k in range(t):
    a,b=map(int,input().split())
    s=input()
    while (b):
        r=s[:b]
        s=r[::-1]+s[b:]
        b-=1
    print(s)