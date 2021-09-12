

from winfetch.sysmfy import *
import winfetch.ascii_logos as logo


banner_name = logo.windows


sysfo = {}


sysfo["Platform"] = platform_name
sysfo["Host_name"] = host_name
sysfo["OS"] = os_version
sysfo["Kernel"] = kernel
sysfo["uptime"] = uptime
sysfo["Resolution"] = screensize
#sysfo["Architecure"] = processor_architecture
#sysfo["Cpus-Freq"] = cpu_frequency[0]/100
#sysfo["Cpu_model"] = cpu_name
#sysfo["GPU_model"] = gpu_name
sysfo["memory"] = f"{available_memory} / {total_memory} ( {memory_usage_percent}% )"



