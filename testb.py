

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    return uptime_seconds




# python script showing battery details
import psutil

import timeit

print(timeit.timeit('ut.uptime2()'))