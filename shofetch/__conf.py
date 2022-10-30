
from shofetch.sysmfy import *
import shofetch.ascii_logos as logo
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

sysfo[uptime_text] = uptime()
sysfo[packages_text] = packages()
sysfo[shell_text] = shell()
sysfo[resolution_text] = screensize()
sysfo[wm_text] = desktop_manager()

# sysfo[build_text] = build_version()
# sysfo[taskcount_text] = tasks()
# sysfo[battery_percent_text] = battery_percent()

sysfo[terminal_text] = terminal()
sysfo[cpu_text] = cpu_name()
sysfo[gpu_text] = gpu_name()
sysfo[memory_text] = memory_info()
sysfo[storage_text] = disk_information()









# print(end-start)

#cpu threads
#data and time
#localip / public ip
#harddisk information
#shell name


# sysfo[memory_text] = f"{available_memory} / {total_memory} ( {memory_usage_percent}% )"
# sysfo[battery_runtime_text] = battery_runtime()
# sysfo[cpu_text] = f"{cpu_name()} @ {cpu_frequency()[2]/1000} GHz"
# sysfo["Cpus-Freq "] = f"{cpu_frequency()[2]/1000} gHZ"


# lst = [os_version,gpu_name,cpu_name,uptime,kernel,shell,terminal,desktop_manager,memory_info,disk_information]
# def confs_getter():

#     sysfo = {}
#     
#     with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
#         
#         # sysfo = [executor.submit(l) for l in lst]

#         # sysfo[resolution_text] = executor.submit(screensize).result()

#         # sysfo[uptime_text] = executor.submit(uptime).result()

#         # sysfo[build_text] =           executor.submit(build_version).result()
#         # sysfo[battery_percent_text] = executor.submit(battery_percent).result()

#         sysfo[os_text] =      executor.submit(os_version).result()
#         sysfo[kernel_text] =  executor.submit(kernel).result()
#         sysfo[uptime_text] =  executor.submit(uptime).result()
#         sysfo[packages_text] = executor.submit(packages).result()
#         sysfo[shell_text] =   executor.submit(shell).result()
#         sysfo[resolution_text] =   executor.submit(screensize).result()
#         sysfo[wm_text] =     executor.submit(desktop_manager).result()
#         sysfo[terminal_text]= executor.submit(terminal).result()
#         sysfo[taskcount_text] =       executor.submit(tasks).result()
#         sysfo["Cpu_model "] = executor.submit(cpu_name).result()
#         sysfo[gpu_text] =     executor.submit(gpu_name).result()
#         sysfo[memory_text] =  executor.submit(memory_info).result()
#         sysfo[storage_text] = executor.submit(disk_information).result()
#     
#     return sysfo
#     


