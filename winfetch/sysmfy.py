from subprocess import Popen, PIPE
from pprint import pprint
from colorama import Fore
import platform 
import psutil
import time , os
import datetime



#objects

processor = psutil.Process()
memory = psutil.virtual_memory()


#win_shell_commands

WIN_GPU ="powershell \"Get-CimInstance -ClassName Win32_VideoController -Property caption|Select-Object caption \"" 
WIN_CPU = "wmic cpu get name"


#Unix_Shell_commands

SCREEN_RES_LINUX = "xdpyinfo| grep dimension| awk '{print $2}'"
LINUX_KERNEL = "uname -r"
CPU_MODEL = "cat /proc/cpuinfo |grep 'model name' | cut -d \":\" -f 2| head -n1"
ARCHITECTURE = "uname -m"
GPU_MODEL = "lspci |grep VGA |cut -d ':' -f3"


#  powershell "Get-CimInstance -ClassName Win32_VideoController -Property *"


def stdout_control(cmd):
	output = Popen(SCREEN_RES_LINUX,shell=True, stdout=PIPE).communicate()[0]
	return output.decode().strip()


def win_get_gpu():
	output = Popen(WIN_GPU,shell=True, stdout=PIPE).communicate()[0].decode().split("\n")
	return output[3]



def win_get_cpu():
	output = Popen(WIN_CPU,shell=True, stdout=PIPE).communicate()[0].decode().split("\n")
	return output[1].strip()


#hardware_information_variables


platform_name = platform.system()
cpu_frequency  = psutil.cpu_freq()
total_cores = os.cpu_count()
cpu_frequency  = psutil.cpu_freq()


#os_informations_variables
host_name = platform.uname().node
os_version = platform.uname().release
raw_uptime = psutil.boot_time()
uptime = datetime.datetime.fromtimestamp(raw_uptime).strftime("%H:%M:%S")


#memory_related_variables
total_memory =( memory.total // 1024 ** 2)
available_memory = (memory.available // 1024 ** 2 )
memory_usage_percent = memory.percent


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
	processor_architecture = stdout_control(ARCHITECTURE)
	kernel = stdout_control(LINUX_KERNEL)
	cpu_name = stdout_control(CPU_MODEL)
	gpu_name = stdout_control(GPU_MODEL)

	