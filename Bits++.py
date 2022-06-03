c=0
t=int(input())
for i in range(t):
    s=input()
    if s=='++X':
        c+=1
    if s=='--X':
        c-=1
    if s=='X++':
        c+=1
    if s=='X--':
        c-=1
print(c)