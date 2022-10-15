#import necessary library
from time import strftime
import time
def clock():
    while True:
        current_time = strftime('%D %H:%M:%S%p')
        time.sleep(1)
        print(current_time)
clock()  

