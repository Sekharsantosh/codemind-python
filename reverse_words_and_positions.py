n=input()
k=n.split()
m=[i[::-1] for i in k]
h=" ".join(reversed(m))
print(h)
