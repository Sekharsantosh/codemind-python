n=int(input())
k=0
j=0
c=0
while n:
    r=n%10
    if(r%2==0):
        k=1
    elif (r%2==1):
        j=1
    n=n//10
if k==1 and j==1:
    print("Mixed")
elif k==1 :
    print("Even")
else:
    print("Odd")