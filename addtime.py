import datetime
import time
i = 5
time1 = datetime.datetime.strptime("2018-10-18 18:50:57.606989",'%Y-%m-%d %H:%M:%S.%f')
print("Time1:",time1)
while( i <= 100):
    print(time1  +  datetime.timedelta(minutes = i)) # adds 5 minutes to the time1
    time.sleep(2)
    i = i + 5

