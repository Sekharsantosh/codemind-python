n=int(input())
s=[]
for i in range(n):
    d=input()
    s.append(d)

for i in s:
    if(len(i)%2==0 and i[::-1]==i):
        print("YES EVEN")
    elif(len(i)%2!=0 and i[::-1]==i):
        print("YES ODD")
    else:
        print("NO")