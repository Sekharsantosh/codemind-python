n=input()
n=n.lower()
v="aeiou"
c=0
k=0
for i in n:
    if i in v:
        c=c+1
        k=1
if k==0:
    print("0")
else:
      print(c)