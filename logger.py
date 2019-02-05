import logging,time
import datetime
from logging.handlers import RotatingFileHandler
##logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
##logging.warning(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' This will get logged to a file')
##logging.debug(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' This will get logged to a Debug')
##logging.info(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' This will get logged to a file')
##logging.error(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' This will get logged to a file')
##logging.critical(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' This will get logged to a file')

log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

logFile = 'app.log'

my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=200, 
                                 backupCount=2, encoding=None, delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.DEBUG)

app_log = logging.getLogger('root')
app_log.setLevel(logging.DEBUG)

app_log.addHandler(my_handler)
c = 1
while c <= 20:
    time.sleep(1)
    #app_log.info("data")
    app_log.debug(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' This will get logged to a Debug')
    c += 1
