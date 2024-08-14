import time
current=time.localtime(time.time())
y=current.tm_hour
if y<12:
    print("AM ")
else:
    print("PM")    