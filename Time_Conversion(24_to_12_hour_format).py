from datetime import datetime
n=input()
d = datetime.strptime(n, "%H:%M")
d=d.strftime("%I:%M %p")
print(d)