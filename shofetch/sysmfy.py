from subprocess import Popen, PIPE
from pprint import pprint
from colorama import Fore
import platform 
import psutil
import time , os
import datetime
import shutil


#objects

processor = psutil.Process()
memory = psutil.virtual_memory()


#win_shell_commands

WIN_GPU ="powershell \"Get-CimInstance -ClassName Win32_VideoController -Property caption|Select-Object caption \"" 
WIN_CPU = "wmic cpu get name"
UPTIME_WIN = "powershell (get-date) - (gcim Win32_OperatingSystem).LastBootUpTime"


#Unix_Shell_commands

SCREEN_RES_LINUX = "xrandr | grep '*' | cut -d' ' -f 4"
LINUX_KERNEL = "uname -r"
CPU_MODEL = "cat /proc/cpuinfo |grep 'model name' | cut -d \":\" -f 2| head -n1"
ARCHITECTURE = "uname -m"
GPU_MODEL = "lspci |grep VGA |cut -d ':' -f3"
OS_NAME = "cat /etc/os-release | grep NAME | head -1 | cut -d'\"' -f 2"
MEM_INFO = "free | grep Mem  | awk '{print $2}' "
SHELL_NAME = "which $SHELL"
UPTIME_UNIX = "cat /proc/uptime | cut -d \" \" -f1"

#Defferent Based Linux Command

ARCH_PACK = "pacman -Q | wc -l"
DEBIAN_PACK = "apt list --installed | wc -l"


#  powershell "Get-CimInstance -ClassName Win32_VideoController -Property *"


def stdout_control(cmd):
	output = Popen(cmd,shell=True, stdout=PIPE).communicate()[0]
	return output.decode().strip()



#win_things

def win_ver():
	vercmd = " ".join(platform.platform().split(".")[0].split("-")[:2])
	return vercmd


def build_ver():
	cmd = platform.platform().split(".")[2].split("-")[0]
	return cmd

def win_uptime():
	upcmd = stdout_control(UPTIME_WIN)
	raw_uptime = upcmd.split("\n")[1:4]
	list_uptime = [x.split(":")[1].strip() for x in raw_uptime]
	context = f"{list_uptime[0]} hour {list_uptime[1]} min"
	return context 

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

def unix_shell_name():
    return stdout_control(SHELL_NAME)

def unix_terminal_name():
    return os.environ["TERM"]

def unix_desktop_name():
    return os.environ["DESKTOP_SESSION"]


def unix_package_list():
    base = 'arch'
    
    if base == 'arch':
        amount = stdout_control(ARCH_PACK)
    elif base == 'debian':
        amount = stdout_control(DEBIAN_PACK)

    return amount
        


def unix_uptime():
    
    
    raw_sec = float(stdout_control(UPTIME_UNIX))


    def convert(seconds):
         seconds = seconds % (24 * 3600)
         hour = seconds // 3600
         seconds %= 3600
         minutes = seconds // 60
         seconds %= 60
         
         if int(hour) < 1:
             return f"{int(minutes)} min"
     
         return f"{ int(hour)} hour {int(minutes)} min"
     
    
    converted_uptime = convert(raw_sec)

    return converted_uptime






    uptime2 = "uptime |awk -F'[:, ]' '{print $7\"h\" \" \"$8\"m\"}'"
    return stdout_control(uptime2)

def unix_total_memory():
    return stdout_control("free | grep Mem  | awk '{print $2}' ")

def unix_used_memory():
    return stdout_control("free | grep Mem  | awk '{print $3}' ")

def unix_free_memory():
    return stdout_control("free | grep Mem  | awk '{print $4}' ")



#Global Funcs

def disk_info():
    disk = shutil.disk_usage(".")
    disk_used = round((( disk.free ) / 1024**3),2)
    disk_total = round(((  disk.total ) / 1024**3),2 )
    free_disk = round((( disk_used / disk_total ) * 100),2)
    
    context = f"{disk_used} / {disk_total} ({free_disk}% free)"

    return context





#hardware_information_variables


platform_name = platform.system
cpu_frequency  = psutil.cpu_freq
total_cores = os.cpu_count
cpu_frequency  = psutil.cpu_freq


#os_informations_variables
host_name = platform.uname
#os_version = platform.uname().release
#raw_uptime = psutil.boot_time()
#uptime = datetime.datetime.fromtimestamp(raw_uptime).strftime("%H:%M:%S")

# uptime = unix_uptime

#memory_related_variables
total_memory =( memory.total // 1024 ** 2)
available_memory = (memory.available // 1024 ** 2 )
memory_usage_percent = memory.percent


#storage related info

disk_sec = disk_info
 







if platform_name() == "Windows":
	
	screensize = win_screensize
	processor_architecture = win_processor_arch
	kernel = win_kernel
	os_version = win_ver
	build_version = build_ver
	gpu_name = win_gpu
	cpu_name = win_cpu #f"{win_cpu()} @ { cpu_frequency[2]/100 } GHz "
	uptime = win_uptime

else:

	screensize = unix_screensize
	processor_architecture = unix_processor_arch
	kernel = unix_kernel
	cpu_name = unix_cpu  #f"{stdout_control(CPU_MODEL)} @ {cpu_frequency} GHz"
	gpu_name = unix_gpu
	os_version = unix_os_version
	packages = unix_package_list
	shell = unix_shell_name
	terminal = unix_terminal_name
	desktop_manager = unix_desktop_name
	uptime = unix_uptime

	# total_memory = unix_total_memory
	# available_memory = unix_free_memory
	# memory_usage_percent = int(unix_used_memory()) / (int(unix_total_memory()) * 100 )

