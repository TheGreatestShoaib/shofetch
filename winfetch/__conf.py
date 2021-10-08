from winfetch.sysmfy import *
import winfetch.ascii_logos as logo


#banner_name = logo.arch
banner_name = logo.small_arch 




sysfo = {}


#sysfo["Platform"] = platform_name()
#sysfo["Host_name"] = host_name().node
sysfo["OS"] = os_version()
#sysfo["Host_name"] = host_name().node
#sysfo["Kernel"] = kernel()
sysfo["uptime"] = uptime
sysfo["Resolution"] = screensize()
#sysfo["Architecure"] = processor_architecture()
#sysfo["Cpus-Freq "] = f"{cpu_frequency()[2]/1000} gHZ"
#sysfo["Cpu_model "] = cpu_name()
sysfo["CPU"] = f"{cpu_name()} @ {cpu_frequency()[2]/1000} GHz"
#sysfo["GPU_model "] = gpu_name()
sysfo["memory "] = f"{total_memory-available_memory} / {total_memory} ( {memory_usage_percent}% )"



#cpu threads
#battery
#data and time
#localip / public ip
#harddisk information
#shell name
