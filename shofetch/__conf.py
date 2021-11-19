from shofetch.sysmfy import *
import shofetch.ascii_logos as logo
#import emojis

#from shofetch.icons.chinese import *
from shofetch.icons.chinese import *


theme = "default"
msg_type = "custom"
banner_name = logo.small_arch
sysfo = {}

#sysfo["Platform"] = platform_name()
#sysfo[gpu_text+"1"] = host_name().node
sysfo[os_text] = os_version()
#sysfo[cpu_text+"1"] = host_name().node

#sysfo[os_text+"1"] = kernel()
sysfo[uptime_text] = uptime()
#sysfo[cpu_text+"4"] = host_name().node


#sysfo[os_text+"3"] = uptime()
#sysfo[uptime_text+"2"] = uptime()
sysfo[resolution_text] = screensize()


#sysfo[cpu_text+"3"] = processor_architecture()
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



