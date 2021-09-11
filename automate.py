
from subprocess import Popen, PIPE
from pprint import pprint
from colorama import Fore
import platform , ctypes
import GPUtil ,psutil
import time , os
import cpuinfo
import datetime


from winfetch_core import logo

#colors 
green = Fore.GREEN
cyan = Fore.CYAN
white = Fore.WHITE


dummy = "."
os.system("cls")

banner = logo.windows.split("\n")

#functions {

def limit_determiner(banner):
    highest_val = 0 
    for line in banner:
        if len(line) > highest_val:
            highest_val = len(line)

    return highest_val



def return_cmd(command):
    process = Popen(args=command,stdout=PIPE,shell=True)
    return str(process.communicate()[0])


#}

#objects
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
total_memory =( memory.total // 1024 ** 2)
available_memory = (memory.available // 1024 ** 2 )
memory_usage_percent = memory.percent


def cpu_info():
    pass




# info_dict = {
#     "host_name":host_name,
#     "Windows -v":os_version,
#     "Resolution":f"{screensize[0]}X{screensize[1]}",
#     "uptime":uptime,
#     "CPU":cpu_name,
#     "GPU":gpu_name,
#     "memory":f"{available_memory} / {total_memory} ( {memory_usage_percent}% )",
#     "Cpu-Freq": cpu_frequency[0]/1000,
# }

info_dict = {
    0:("host_name",host_name),
    1:("Windows -v",os_version),
    2:("Resolution",f"{screensize[0]}X{screensize[1]}"),
    3:("uptime",uptime),
    4:("CPU",cpu_name),
    5:("GPU",gpu_name),
    6:("memory",f"{available_memory} / {total_memory} ( {memory_usage_percent}% )"),
    7:("Cpu-Freq",cpu_frequency[0]/1000),
    8:("Resolution",f"{screensize[0]}X{screensize[1]}"),
    9:("uptime",uptime),
    10:("CPU",cpu_name),




}




x = 0
limits = limit_determiner(banner)
whitespace = "    "
seperator = " : "


for i in range(len(banner)):


    try:
        #print(green ,banner[i], whitespace , cyan , key , seperator , white , value )
        key = info_dict[i][0]
        value= info_dict[i][1]

        if not len(banner[i]) < limits:
            #print(len(banner[i]))
            print(green ,banner[i], whitespace , cyan , key , seperator , white , value )
        else:
            print(" " * ( limits - len(banner[i]) ) , cyan, "      " , key , seperator , white,value)

    except KeyError:
        print(green,banner[i])







# for key,value in info_dict.items():
#     #if x <= len(info_dict):

#     if not len(banner[x]) < limits:
#         #print(len(banner[x-1]))
#         print(green,banner[x],cyan,"   ",key,":",white,value)
#     else:
#         print(" "* (limits-len(banner[x])),cyan,"     ",key,":",white,value)
    
#     x +=1





#cmd = return_cmd("powershell \"gps | where {$_.MainWindowTitle } | select Description ").replace(r"\r","").split("\\n")




