n=input()
c=0
n=n.upper()
n=n.split()
n="".join(n)
for i in n:
        i=ord(i)
        if i not in range(65,91):
                if i not in range(48,58):
                #print(j,end=" ")
                       c=c+1
print(c)           
         