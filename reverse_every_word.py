n=input()
k=n.split()
nn=[i[::-1] for i in k]
j=" ".join(nn)
print(j,end="")