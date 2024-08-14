from datetime import datetime
now=datetime.now()
year=now.strftime("%y")
print("year:",year)
month=now.strftime("%m")
print("month:",month)
day=now.strftime("%d")
print("day:",day)
time=now.strftime("%H:%M:%S")
print("TIME:",time)
date_time=now.strftime("%m/%d/%y,%H:%M:%S")
print("dATE AND TIME:",date_time)

