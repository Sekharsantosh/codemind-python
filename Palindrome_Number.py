def reverse(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
l=[]
n=int(input())
for i in range(0,n):
    e=int(input())
    l.append(e)
for i in l:
    if reverse(i)==i:
        print(True)
    else:
        print(False)