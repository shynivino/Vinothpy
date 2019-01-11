import datetime
import time
i = 5
print(datetime.date.today().strftime('%Y-%m-%d'))
time1 = datetime.datetime.strptime(str(datetime.date.today().strftime('%Y-%m-%d')),'%Y-%m-%d')
print("Time1:",str(time1)[:10])
#while( i <= 100):
time2= str(time1  +  datetime.timedelta(days = -7))
print(time2[:10]) # adds 5 minutes to the time1

