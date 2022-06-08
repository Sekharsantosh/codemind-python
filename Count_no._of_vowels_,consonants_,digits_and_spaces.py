n=input()
k=0
d=0
v=0
c=0
j="aeiou"
x=n.split()
for i in n:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        if i in j:
            v=v+1
        else:
            c=c+1
    elif i==" ":
        k=k+1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",k)