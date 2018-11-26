# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 15:18:40 2018

@author: Reach User2
"""

import os
import datetime
last_mod_time = os.path.getmtime("sklearn_program.py")

last_mod_time = datetime.datetime.fromtimestamp(last_mod_time)
print(last_mod_time)

cur_time = datetime.datetime.now()
print(cur_time)

time_delta = (cur_time-last_mod_time)
print(time_delta)
print(divmod(time_delta.total_seconds(),60)[0]/60) #print no of hours 
