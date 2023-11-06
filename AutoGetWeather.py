import os
import time

with open('log.txt','w+') as f:
    f.write(str(time.asctime( time.localtime(time.time()) )))