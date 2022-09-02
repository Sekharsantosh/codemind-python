n=input()
vowels="aeiou"
k=0
for i in vowels:
    if i not in n:
        print(i,end=" ")
        k=1
if k==0:
        print("0")