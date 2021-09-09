
from subprocess import Popen, PIPE
from pprint import pprint
from colorama import Fore
import cpuinfo
import datetime
import platform
import ctypes
import GPUtil
import psutil
import time
import os


green = Fore.GREEN
cyan = Fore.CYAN
white = Fore.WHITE


dummy = "."

os.system("cls")

def return_cmd(command):
    process = Popen(args=command,stdout=PIPE,shell=True)
    return str(process.communicate()[0])



#os name
#processor name



user32 = ctypes.windll.user32
processor = psutil.Process()
memory = psutil.virtual_memory()
GPUs = GPUtil.getGPUs()
cpu_name = cpuinfo.get_cpu_info()["brand_raw"]




#hardware_information_variables
total_cores = psutil.cpu_count()
cpu_frequency  = psutil.cpu_freq()
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
gpu_name =GPUtil.getGPUs()[0].name



#os_informations_variables
host_name = platform.uname().node
os_version = platform.uname().release
raw_uptime = psutil.boot_time()
uptime = datetime.datetime.fromtimestamp(raw_uptime).strftime("%H:%M:%S")



#memory_related_variables
total_memory = memory.total
available_memory = memory.available
memory_usage_percent = memory.percent


#cmd = return_cmd("powershell \"gps | where {$_.MainWindowTitle } | select Description ").replace(r"\r","").split("\\n")



banner = f"""
{green}
{green}                            .oodMMMM {cyan}  Host Name    :{white} {host_name}
{green}       ..oodMMM  MMMMMMMMMMMMMMMMMMM {cyan}  Windows -v   :{white} {os_version}
{green} oodMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}  Resolution   :{white} {screensize[0]}X{screensize[1]}
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}  Uptime       :{white} {uptime}
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}  .            :{white} .
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}  .            :{white} .
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}  Cpu-Frequency:{white} { cpu_frequency[0]/1000 }
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}  .            :{white} {dummy}
{cyan       }                                       .            :{white} {dummy}
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}  .            :{white} .
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}  .            :{white} .
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}  .            :{white} . 
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}  .            :{white} .
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}  .            :{white} .
{green} `^^^^^^MMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}  CPU          :{white} {cpu_name}
{green}       ````^^^^  ^^MMMMMMMMMMMMMMMMM {cyan}  GPU          :{white} {gpu_name}
{green}                      ````^^^^^^MMMM {cyan}  Memory       :{white} {dummy}


"""

print(banner)

# print(cpu_frequency)
# print(available_memory)