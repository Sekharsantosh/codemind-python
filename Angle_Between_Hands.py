s=input()
h=((ord(s[0])-48)*10+ord(s[1])-48)
m=((ord(s[3])-48)*10+ord(s[4])-48)
angle=(11/2)*m-30*h
if angle<0:
    angle+=360
if angle>180:
    angle=360-angle
print("{:.1f}".format(angle))