n,p,r=map(int,input().split())
if n>50 and p>60 and r>100:
    print("10")
elif n>50 and p>60 and r<100:
    print("9")
elif n<50 and p>60 and r>100:
    print("8")
elif n>50 and p<60 and r>100:
    print("7")
elif n>50 or p>60 or r>100:
    print("6")
else:
    print("5")