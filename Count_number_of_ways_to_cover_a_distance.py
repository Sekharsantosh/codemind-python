def dist(n):
    if n<0:
        return 0;
    elif n==0:
        return 1;
    else:
        return dist(n-1)+dist(n-2)+dist(n-3)


n=int(input())
k=dist(n)
print(k)
