def palindrome(n):
    t=n
    rev=0
    while t:
        r=t%10
        rev=rev*10+r
        t=t//10
    if n==rev:
        return True
    else:
        return False
n=int(input())
#print(n)
s=0
d=0
f=0
k=n
while True:
    k=k+1
    if palindrome(k):
        d=k
        break
s=n
while True:
    s=s-1
    if palindrome(s):
        f=s
        break
#print(f,d)
if d-n<n-f:
    print(d)
elif d-n>n-f:
    print(f)
else:
    print(f,d)