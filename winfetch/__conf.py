

from winfetch.sysmfy import *
import winfetch.ascii_logos as logo


banner_name = logo.mac


sysfo = {}

sysfo["host_name"] = host_name
sysfo["Windows -v"] = os_version
sysfo["Resolution"] = (screensize[0],screensize[1])
sysfo["uptime"] = uptime
sysfo["Cpu"] = cpu_name
sysfo["GPU"] = gpu_name
sysfo["memory"] = f"{available_memory} / {total_memory} ( {memory_usage_percent}% )"
sysfo["Cpus-Freq"] = cpu_frequency[0]/100
sysfo["Windowss -v"] = os_version
sysfo["Resolsution"] = (screensize[0],screensize[1])
sysfo["uptimse"] = uptime

