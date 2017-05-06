from datetime import datetime
from threading import Timer

x=datetime.today()
print(x.minute)
y=x.replace(day=x.day+1, hour=11, minute=7, second=0, microsecond=0)#Will run on next day 11:07:00AM 
#y=x.replace(minute=x.minute+1, second=0, microsecond=0) #Will run in next minute
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    print ("hello world")
    
t = Timer(secs, hello_world)
t.start()
