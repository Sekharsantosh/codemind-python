n=int(input())
for i  in range(1,n+1):
    for j in range(1,n-1):#5//2=2+1
          print(j,end="")
    for k in reversed(range(1,j)):#santosh coding is fun
          print(k,end="")
    print()