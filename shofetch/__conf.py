from shofetch.sysmfy import *
import shofetch.ascii_logos as logo
import emojis

#from shofetch.icons.chinese import *
from shofetch.icons.chinese import *

msg_type = "chinese"

banner_name = logo.manjaro 


sysfo = {}


#sysfo["Platform"] = platform_name()
#sysfo["Host_name"] = host_name().node
sysfo[os_text] = os_version()
#sysfo["Host_name"] = host_name().node
#sysfo["Kernel"] = kernel()
sysfo[uptime_text] = uptime()
sysfo[resolution_text] = screensize()
#sysfo["Architecure"] = processor_architecture()
#sysfo["Cpus-Freq "] = f"{cpu_frequency()[2]/1000} gHZ"
#sysfo["Cpu_model "] = cpu_name()
sysfo[cpu_text] = f"{cpu_name()} @ {cpu_frequency()[2]/1000} GHz"
#sysfo[gpu_text] = gpu_name()

sysfo[memory_text] = f"{available_memory} / {total_memory} ( {memory_usage_percent}% )"



#cpu threads
#battery
#data and time
#localip / public ip
#harddisk information
#shell name



