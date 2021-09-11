from subprocess import Popen, PIPE
from pprint import pprint
from colorama import Fore
import platform 
import GPUtil ,psutil
import time , os
import cpuinfo
import datetime



#objects

processor = psutil.Process()
memory = psutil.virtual_memory()
GPUs = GPUtil.getGPUs()
cpu_name = cpuinfo.get_cpu_info()["brand_raw"]


SCREEN_RES_LINUX = "xdpyinfo| grep dimension| awk '{print $2}'"

#hardware_information_variables

platform_name = platform.system()
	

if platform_name == "Windows":
	import ctypes
	user32 = ctypes.windll.user32
	screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
else:
	screensize = Popen(SCREEN_RES_LINUX,shell=True, stdout=PIPE).communicate()[0]




total_cores = psutil.cpu_count()
cpu_frequency  = psutil.cpu_freq()

gpu_name =GPUtil.getGPUs()[0].name



#os_informations_variables
host_name = platform.uname().node
os_version = platform.uname().release
raw_uptime = psutil.boot_time()
uptime = datetime.datetime.fromtimestamp(raw_uptime).strftime("%H:%M:%S")



#memory_related_variables
total_memory =( memory.total // 1024 ** 2)
available_memory = (memory.available // 1024 ** 2 )
memory_usage_percent = memory.percent