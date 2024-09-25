
from shofetch.sysmfy import *
import shofetch.ascii_logos as logo





# Please Do Not Modify Anything Above This Line Without Knowing What You Are Doing...



from shofetch.icons.normal import *
# from shofetch.icons.chinese import *


#Themes are presets of how your information is displayed; in other words, it is the overall layout.
#In-built themes are: gradient, centered.

theme = "default"
# theme = "midway"



#msg_type determines which message will be printed below the information.
#Available options are: arabic, chinese, random, custom.

#msg_type = "arabic"
#msg_type = "custom"
#msg_type = "random"
# msg_type = "chinese"
msg_type = "custom"
word = "devoured by her smile and now suffocating for her stupidity "
custom_msg_txt = word
custom_msg_padding = 8

# Logos : arch,brh,mac,manjaro,small_arch,linux,android,windows_v2
banner_name = logo.arch
# banner_name = logo.small_arch # arch 


""" 

You can customize what information to show.
Comment out the information you don't by putting a # infront of the line.
To quick-customize the information label, you can put the custom text between [ ].
e.g. sysfo["custom cpu text"].
A static value can also be implemented simply by declaring it as a text for fast performance.

"""

sysfo = {}


sysfo[os_text] = os_version()
sysfo[kernel_text] = kernel()
sysfo[uptime_text] = uptime()

sysfo[uptime_text] = uptime()
sysfo[packages_text] = packages()
sysfo[shell_text] = shell()
sysfo[resolution_text] = screensize()
sysfo[wm_text] = desktop_manager()

# sysfo[build_text] = build_version()
sysfo[taskcount_text] = tasks()

# sysfo[battery_percent_text] = battery_percent()

sysfo[terminal_text] = terminal()
sysfo[cpu_text] = cpu_name()
sysfo[gpu_text] = gpu_name()
sysfo[memory_text] = memory_info(load=True) #load True shows memory load percentage while False shows free space percentage.
sysfo[storage_text] = disk_information()



