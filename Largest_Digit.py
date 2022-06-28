n=int(input())
a=[]
while(n):
    r=n%10
    a.append(r)
    n=n//10
print(max(a))