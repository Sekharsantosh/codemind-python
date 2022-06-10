n=input()
n=n.split()
for i in range(0,len(n)):
    if i%2==0:
        k=n[i]
        k=k[::-1]
        n.remove(n[i])
        n.insert(i,k)
print(*n)