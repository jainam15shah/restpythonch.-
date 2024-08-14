import time
current=time.localtime(time.time())
y=current.tm_hour
if y<=12:
    print("hour",y)
elif y==13:
    print("hour 1 ")
elif y==14:
    print("hour 2 ")
elif y==15:
    print("hour 3 ")
elif y==16:
    print("hour 4 ")
elif y==17:
    print("hour 5 ")
elif y==18:
    print("hour 6 ")
elif y==19:
    print("hour 7 ")
elif y==20:
    print("hour 8 ")
elif y==21:
    print("hour 9 ")
elif y==22:
    print("hour 10 ")
elif y==23:
    print("hour 11 ")

else:
    print("hour 12 AM ")
