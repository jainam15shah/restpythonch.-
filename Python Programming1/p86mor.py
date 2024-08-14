import time
current=time.localtime(time.time())
y=current.tm_hour
if y<12:
    print("good morning ")
elif 17<=y<21:
    print("good evening ")
else:
    print("good night")    