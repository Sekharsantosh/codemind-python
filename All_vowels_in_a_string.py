n=input()
vowels="aeiou"
k=0
for i in vowels:
     if i in n:
           k=1
     else:
         k=0
         break
if k==1:
    print("True")
else:
    print("False")