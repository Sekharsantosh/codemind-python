def fact(n):
     s=0
     for i in range(1,n):
         if n%i==0:
             s=s+i
     if s>n:
         return True
     else:
         return False
n=int(input())
if fact(n):
    print("True")
else:
    print(False)