import os
import datetime
import time

while True:
    now  = datetime.datetime.now()
    yesterday = datetime.timedelta(seconds=1)
    result = now + yesterday

    if now < result:
        print("Men o'chdim")
        time.sleep(3)
        os.system('shutdown /s /t 1')