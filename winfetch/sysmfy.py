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

SCREEN_RES_LINUX = "xrandr | grep '*' | cut -d' ' -f 4"
LINUX_KERNEL = "uname -r"
CPU_MODEL = "cat /proc/cpuinfo |grep 'model name' | cut -d \":\" -f 2| head -n1"
ARCHITECTURE = "uname -m"
GPU_MODEL = "lspci |grep VGA |cut -d ':' -f3"
OS_NAME = "cat /etc/os-release | grep NAME | head -1 | cut -d'\"' -f 2"


#  powershell "Get-CimInstance -ClassName Win32_VideoController -Property *"


def stdout_control(cmd):
	output = Popen(cmd,shell=True, stdout=PIPE).communicate()[0]
	return output.decode().strip()



#win_things


def win_gpu():
	output = Popen(WIN_GPU,shell=True, stdout=PIPE).communicate()[0].decode().split("\n")
	return output[3]



def win_cpu():
	output = Popen(WIN_CPU,shell=True, stdout=PIPE).communicate()[0].decode().split("\n")
	return output[1].strip()


def win_processor_arch():
	return os.environ["PROCESSOR_ARCHITECTURE"]

def win_screensize():
	import ctypes
	user32 = ctypes.windll.user32
	screen = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
	screensize = f"{screen[1]}x{screen[1]} Pixels"

	return screensize


def win_kernel():
	return os.environ["OS"]




#unix_things

def unix_processor_arch():
	return stdout_control(ARCHITECTURE)

def unix_screensize():
	return stdout_control(SCREEN_RES_LINUX)

def unix_gpu():
	return stdout_control(GPU_MODEL)

def unix_cpu():
	return stdout_control(CPU_MODEL)

def unix_kernel():
	return stdout_control(LINUX_KERNEL)

def unix_os_version():
	return stdout_control(OS_NAME)

def unix_uptime():
    uptime2 = "uptime |awk -F'[:, ]' '{print $7\"h\" \" \"$8\"m\"}'"
    return stdout_control(uptime2)


#hardware_information_variables


platform_name = platform.system
cpu_frequency  = psutil.cpu_freq
total_cores = os.cpu_count
cpu_frequency  = psutil.cpu_freq


#os_informations_variables
host_name = platform.uname
#os_version = platform.uname().release
raw_uptime = psutil.boot_time()
uptime = datetime.datetime.fromtimestamp(raw_uptime).strftime("%H:%M:%S")

#uptime = unix_uptime

#memory_related_variables
total_memory =( memory.total // 1024 ** 2)
available_memory = (memory.available // 1024 ** 2 )
memory_usage_percent = memory.percent


if platform_name() == "Windows":
	
	screensize = win_screensize
	processor_architecture = win_processor_arch
	kernel = win_kernel
	os_version = platform.platform
	gpu_name = win_gpu
	cpu_name = win_cpu #f"{win_cpu()} @ { cpu_frequency[2]/100 } GHz "

else:

	screensize = unix_screensize
	processor_architecture = unix_processor_arch
	kernel = unix_kernel
	cpu_name = unix_cpu  #f"{stdout_control(CPU_MODEL)} @ {cpu_frequency} GHz"
	gpu_name = unix_gpu
	os_version = unix_os_version

