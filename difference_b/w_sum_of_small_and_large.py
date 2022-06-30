n=input()
n=n.split()
s=0
c=0
for i in n:
    s=s+ord(min(i))
    c=c+ord(max(i))
print(abs(s-c))