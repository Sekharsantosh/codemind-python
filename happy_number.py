def happy(n):
    s=0
    while(n):
        r=n%10
        s=s+r**2
        n=n//10
    if s<9:
        return s
    else:
        return happy(s)
n=int(input())
if happy(n)==1 or happy(n)==7:
    print(True)
else:
    print(False)