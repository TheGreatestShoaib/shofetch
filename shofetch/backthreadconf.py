from shofetch.sysmfy import *
import shofetch.ascii_logos as logo
#import emojis

#from shofetch.icons.nature import *
from shofetch.icons.normal import *



theme = "default"
# theme = "midway"


#msg_type = "arabic"
#msg_type = "custom"
#msg_type = "random"

msg_type = "chinese"
#msg_type = "defualt"



# Logos : arch,brh,mac,manjaro,small_arch,linux,android,windows_v2


banner_name = logo.arch

#banner_name = logo.small_arch # arch 
#banner_name = logo.brh
# banner_name = logo.manjaro # manjaro
# banner_name = logo.brh # windoes
#banner_name = logo.linux # linux


sysfo = {}


# sysfo["Platform"] = platform_name()
sysfo[os_text] = os_version()
sysfo[kernel_text] = kernel()
sysfo[uptime_text] = uptime()

sysfo[resolution_text] = screensize()
sysfo[uptime_text] = uptime()

#sysfo[build_text] = build_version()
sysfo[shell_text] = shell()
sysfo[taskcount_text] = tasks()
#sysfo[battery_percent_text] = battery_percent()
#sysfo[battery_runtime_text] = battery_runtime()
sysfo[wm_text] = desktop_manager()

sysfo[terminal_text] = terminal()

#sysfo["Cpus-Freq "] = f"{cpu_frequency()[2]/1000} gHZ"
#sysfo["Cpu_model "] = cpu_name()
sysfo[cpu_text] = f"{cpu_name()} @ {cpu_frequency()[2]/1000} GHz"
sysfo[gpu_text] = gpu_name()
#sysfo[memory_text] = f"{available_memory} / {total_memory} ( {memory_usage_percent}% )"
sysfo[memory_text] = memory_info()

sysfo[storage_text] = disk_information()


#cpu threads
#data and time
#localip / public ip
#harddisk information
#shell name



