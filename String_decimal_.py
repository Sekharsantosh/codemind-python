n=int(input())
s=[]
k=0
for i in range(0,10):
    s.append(i)
for i in range(n):
    
    a=input()
   # print(a)
    for i in a:
        if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
            k=1
        else:
            k=0
            break
    if k==1:
        print(True)
    else:
        print(False)