n=int(input())
a=list(map(int,input().split()))
c=0
t=[]
#print(a)
for i in a:
    if i==1:
        c+=1
    t.append(c)
    if i==0:
        c=0
           
        
print(max(t))