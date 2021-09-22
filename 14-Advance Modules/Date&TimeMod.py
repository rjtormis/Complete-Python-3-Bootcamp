import datetime

myTime = datetime.time(13,20,1,20)
print(myTime)
print(myTime.minute)
print(type(myTime))

today=datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.ctime())

from datetime import datetime
mydatetime=datetime(2021,10,3,14,20,1)
print(mydatetime)
mydatetime=mydatetime.replace(year=2020)
print(mydatetime)

#DATE
from datetime import date
date1= date(2021,11,3)
date2= date(2020,11,3)
result = date1-date2
print(result)
print(result.days)

datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)

result2= datetime1 - datetime2
print(result2)

print(result2.seconds)
print(result2.total_seconds())
