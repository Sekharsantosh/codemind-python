n=input()
d=0
for i in n:
    if i.isdigit():
        d=d+1
if d>0:
  print("Contains",d,"digit")
else:
    print("Doesn't contain digit")