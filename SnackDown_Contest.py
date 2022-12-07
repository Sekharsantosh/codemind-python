def temp(a,ar,br):
    c=[]
    t=[]
    k=0
    for i in br:
        if i not in ar:
            ar.append(i)
    for i in ar:
        if i not in t:
            t.append(i)
            
    for i in range(1,a+1):
          c.append(i)
    for i in c:
        if i in t:
            k=1
        else:
            k=0
            break
    if k==1:
        print("YES")
    else:
        print("NO")
        

t=int(input())
for i in range(t):
    a=int(input())
    ar=list(map(int,input().split()))
    br=list(map(int,input().split()))
    temp(a,ar,br)