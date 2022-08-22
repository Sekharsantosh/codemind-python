def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
t=n
k=n
while True:
    if is_prime(t):
        break
    t=t+1
while True:
    if is_prime(k):
        break
    k=k-1
print(min(t-n ,n-k))
