def isdigit(k):
    for i in k:
        if i.isdigit():
            return True
n=int(input())
a=[]
c=0
for i in range(n):
    e=input()
    a.append(e)
for i in a:
        if isdigit(i):
            c=1
            print("Yes")
        else:
            c=0
            print("No")