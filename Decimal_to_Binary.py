def binary(n):
    s=[]
    while n:
        r=n%2
        s.append(r)
        n=n//2
    return s
n=int(input())
for i in range(n):
    s=0
    a=int(input())
    s=binary(a)
    for i in s[::-1]:
        print(i,end="")
    print()