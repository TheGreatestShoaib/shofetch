
from subprocess import Popen, PIPE
from pprint import pprint
from colorama import Fore
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
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return str(process.communicate()[0])



#os name
#processor name



user32 = ctypes.windll.user32
processor = psutil.Process()
memory = psutil.virtual_memory()


total_cores = psutil.cpu_count()
cpu_frequency  = psutil.cpu_freq()
host_name = platform.uname().node
os_version = platform.uname().release
total_memory = memory.total
memory_usage_percent = memory.percent
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
GPUs = GPUtil.getGPUs()
raw_uptime = psutil.boot_time()
uptime = datetime.datetime.fromtimestamp(raw_uptime).strftime("%H:%M:%S")






# print(total_cores)
# print(cpu_frequency)
# print(f"Host Name : {host_name} ")
# print(f"Total Memory : { round(total_memory/1024**2 ) } MiB")
# print()
# print(f"Memory Usage : { memory_usage_percent }%")
# print(f"Resolution : {screensize[0]}X{screensize[1]}")
# print(f"Uptime : { uptime } ")


cmd = return_cmd("powershell \"gps | where {$_.MainWindowTitle } | select Description ").replace(r"\r","").split("\\n")



# print("cpu parcent:",processor.cpu_percent(interval=1) )

# print("memory : " ,processor.memory_info())




banner = f"""

{green}
{green}                            .oodMMMM {cyan}  Host Name    :{white} {host_name}
{green}       ..oodMMM  MMMMMMMMMMMMMMMMMMM {cyan}  Disk Usage   :{white} {dummy}
{green} oodMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}  Resolution   :{white} {screensize[0]}X{screensize[1]}
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}  Uptime       :{white} {uptime}
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}  Total Memory :{white} {round(total_memory/1024**2 )} Mib
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}   {dummy}
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}   {dummy}

{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}   {dummy}
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}   {dummy}
{green} MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}   {dummy}
{green} `^^^^^^MMMMMMM  MMMMMMMMMMMMMMMMMMM {cyan}   {dummy}
{green}       ````^^^^  ^^MMMMMMMMMMMMMMMMM {cyan}   {dummy}
{green}                      ````^^^^^^MMMM {cyan}   {dummy}


"""

print(banner)