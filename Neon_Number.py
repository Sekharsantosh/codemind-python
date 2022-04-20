n= int(input())
s=n*n
r=0
while s:
    r +=s%10
    s=s//10
if n==r:
    print('Neon Number')
else:
    print('Not Neon Number')