from subprocess import Popen, PIPE
from pprint import pprint
from colorama import Fore
import platform 
#import GPUtil ,psutil
import psutil
import time , os
#import cpuinfo
import datetime


#  powershell "Get-CimInstance -ClassName Win32_VideoController -Property *"

WIN_GPU ="powershell \"Get-CimInstance -ClassName Win32_VideoController -Property caption|Select-Object caption \"" 
WIN_CPU = "wmic cpu get name"


def stdout_control(cmd):
	output = Popen(SCREEN_RES_LINUX,shell=True, stdout=PIPE).communicate()[0].decode().replace("\n","")
	return output.decode().replace("\n","")




def win_get_gpu():
	output = Popen(WIN_GPU,shell=True, stdout=PIPE).communicate()[0].decode().split("\n")
	return output[3]


def win_get_cpu():
	output = Popen(WIN_CPU,shell=True, stdout=PIPE).communicate()[0].decode().split("\n")
	return output[1].strip()


#objects

processor = psutil.Process()
memory = psutil.virtual_memory()
#GPUs = GPUtil.getGPUs()
#cpu_name = cpuinfo.get_cpu_info()["brand_raw"]


SCREEN_RES_LINUX = "xdpyinfo| grep dimension| awk '{print $2}'"
LINUX_KERNEL = "uname -r"
CPU_MODEL = "cat /proc/cpuinfo | grep \"model name\""




#hardware_information_variables

platform_name = platform.system()
	


cpu_frequency  = psutil.cpu_freq()



if platform_name == "Windows":
	
	import ctypes
	user32 = ctypes.windll.user32
	screen = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
	screensize = f"{screen[1]}x{screen[1]} Pixels"
	
	processor_architecture = os.environ["PROCESSOR_ARCHITECTURE"]

	kernel = os.environ["OS"]

	os_version = platform.platform(terse=True)

	gpu_name = win_get_gpu()

	cpu_name = f"{win_get_cpu()} @ { cpu_frequency[2]/100 } GHz "





else:

	screensize = stdout_control(SCREEN_RES_LINUX)
	processor_architecture = ""
	kernel = stdout_control(LINUX_KERNEL)
	cpu_name = ""
	gpu_name = ""

	




total_cores = os.cpu_count()
cpu_frequency  = psutil.cpu_freq()
#gpu_name =GPUtil.getGPUs()[0].name



#os_informations_variables
host_name = platform.uname().node
os_version = platform.uname().release
raw_uptime = psutil.boot_time()
uptime = datetime.datetime.fromtimestamp(raw_uptime).strftime("%H:%M:%S")



#memory_related_variables
total_memory =( memory.total // 1024 ** 2)
available_memory = (memory.available // 1024 ** 2 )
memory_usage_percent = memory.percent