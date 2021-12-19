from subprocess import Popen, PIPE
import platform 
import os
import shutil


class Decorators :
    def only_Linux(func):
        return func

    def only_Windows(func):
        return func


def stdout_control(cmd):
	output = Popen(cmd,shell=True, stdout=PIPE).communicate()[0]
	return output.decode().strip()



#Global Functions :

def disk_info():
    disk = shutil.disk_usage(".")
    disk_used = round((( disk.free ) / 1024**3),2)
    disk_total = round(((  disk.total ) / 1024**3),2 )
    free_disk = round((( disk_used / disk_total ) * 100),2)
    
    context = f"{disk_used} / {disk_total} ({free_disk}% free)"

    return context


class Linux:
    def __init__(self):

        self.SCREEN_RES_LINUX = "xrandr | grep '*' | cut -d' ' -f 4"
        self.LINUX_KERNEL = "uname -r"

        self.CPU_MODEL = "cat /proc/cpuinfo |grep 'model name' | cut -d \":\" -f 2| head -n1"
        self.ARCHITECTURE = "uname -m"
        self.GPU_MODEL = "lspci |grep VGA |cut -d ':' -f3"

        self.OS_NAME = "cat /etc/os-release | grep NAME | head -1 | cut -d'\"' -f 2"
        self.SHELL_NAME = "which $SHELL"
        self.UPTIME_UNIX = "cat /proc/uptime | cut -d \" \" -f1"
        self.UNIX_PROCESS = "ps -u shoaib | awk '{print $4}' | uniq | wc -l "
        
        #rams
       
        self.UNIX_TOTAL_MEM = "free | grep Mem  | awk '{print $2}' "
        self.UNIX_USED_MEM = "free | grep Mem  | awk '{print $2}' "
        self.UNIX_FREE_MEM = "free | grep Mem  | awk '{print $2}' "
        #Defferent Based Linux Command

        self.ARCH_PACK = "pacman -Q | wc -l"
        self.DEBIAN_PACK = "apt list --installed | wc -l"
        self.GET_TERM = "pstree -s $$"


    def processor_architecture(self):
        return stdout_control(self.ARCHITECTURE)

    def screensize(self):
        return stdout_control(self.SCREEN_RES_LINUX)

    def gpu_name(self):
        return stdout_control(self.GPU_MODEL)

    def desktop_name(self):
        return os.environ["DESKTOP_SESSION"]

    def cpu_name(self):
        return stdout_control(self.CPU_MODEL)

    def kernel(self):
        return stdout_control(self.LINUX_KERNEL)

    def os_name(self):
        return stdout_control(self.OS_NAME)

    def shell_name(self):
        return stdout_control(self.SHELL_NAME).split("/")[2]
 
    def process_counts(self):
        return str(int(stdout_control(self.UNIX_PROCESS))-2)
  
    @Decorators.only_Linux
    def desktop_enviroment(self):
        try:
            return os.environ["DESKTOP_SESSION"]
        except:
            return " "


    @Decorators.only_Linux
    def terminal_name(self):
        
        get_term  = stdout_control(self.GET_TERM).split("---")
        x = 0
        while get_term[x] == "systemd":
            x+=1
        term_name = get_term[x]
        return term_name
        

    @Decorators.only_Linux
    def package_list(self):
        base = 'arch'
        
        if base == 'arch':
            amount = stdout_control(self.ARCH_PACK)
        elif base == 'debian':
            amount = stdout_control(self.DEBIAN_PACK)

        return amount


    def meminfo(self):
        total_mem = int(stdout_control(self.UNIX_TOTAL_MEM))
        used_mem = int(stdout_control(self.UNIX_USED_MEM))
        free_mem = total_mem - used_mem
        percent  = round((free_mem / total_mem)*100 ,2)

        context = f"{used_mem} / {total_mem} ( {percent}% free)"

        return context



    def uptime(self):
        
        def convert(seconds):
             seconds = seconds % (24 * 3600)
             hour = seconds // 3600
             seconds %= 3600
             minutes = seconds // 60
             seconds %= 60
             
             if int(hour) < 1:
                 return f"{int(minutes)} min"
         
             return f"{ int(hour)} hour {int(minutes)} min"
         
        
        raw_sec = float(stdout_control(self.UPTIME_UNIX))
        converted_uptime = convert(raw_sec)
        return converted_uptime

        # uptime2 = "uptime |awk -F'[:, ]' '{print $7\"h\" \" \"$8\"m\"}'"
        # return stdout_control(uptime2)


    @Decorators.only_Windows
    def build_version(self):
        pass

    def battery_percentage(self):
        pass

    def battery_runtime(self):
        pass




class Windows:

    def __init__(self):

        self.WIN_GPU ="powershell \"Get-CimInstance -ClassName Win32_VideoController -Property caption|Select-Object caption \"" 
        self.WIN_CPU = "wmic cpu get name"
        self.UPTIME_WIN = "powershell (get-date) - (gcim Win32_OperatingSystem).LastBootUpTime"
        self.WIN_TASKS = "powershell (tasklist).count"
        self.WIN_BATTERY_REMAINING = "powershell (Get-WmiObject win32_battery).estimatedChargeRemaining"
        self.WIN_BATTERY_RUNTIME = "powershell (Get-WmiObject win32_battery).estimatedRunTime"
        self.WIN_FREE_MEM = """powershell (Get-Counter '\Memory\Available MBytes').CounterSamples.CookedValue """
        self.WIN_TOTAL_MEM = 'powershell (get-wmiobject -class "win32_physicalmemory" -namespace "root\CIMV2").Capacity'

    def os_name(self):
        vercmd = " ".join(platform.platform(self).split(".")[0].split("-")[:2])
        return vercmd


    @Decorators.only_Windows
    def build_version(self):
        cmd = platform.platform(self).split(".")[2].split("-")[0]
        return cmd

    def uptime(self):
        upcmd = stdout_control(self.UPTIME_WIN)
        raw_uptime = upcmd.split("\n")[1:4]
        list_uptime = [x.split(":")[1].strip(self) for x in raw_uptime]
        context = f"{list_uptime[0]} hour {list_uptime[1]} min"
        return context 

    def gpu_name(self):
        output = Popen(self.WIN_GPU,shell=True, stdout=PIPE).communicate(self)[0].decode().split("\n")
        return output[3]



    def cpu_name(self):
        output = Popen(self.WIN_CPU,shell=True, stdout=PIPE).communicate(self)[0].decode().split("\n")
        return output[1].strip(self)


    def processor_architecture(self): 
        return os.environ["PROCESSOR_ARCHITECTURE"]

    def kernel(self): 
        kernel = platform.platform(self).split("-")[2]
        return kernel

    def process_counts(self):
        output = stdout_control(self.WIN_TASKS)
        return output

    def battery_percentage(self):
        output =stdout_control(self.WIN_BATTERY_REMAINING)
        return output
    
    def battery_runtime(self):
        output =stdout_control(self.WIN_BATTERY_RUNTIME)
        return output


    @Decorators.only_Linux
    def terminal_name(self):
        pass


    def meminfo(self):
        total_mem = int(stdout_control(self.WIN_TOTAL_MEM))
        free_mem = int(stdout_control(self.WIN_FREE_MEM))
        used_mem = int(int(total_mem) - int(free_mem))
        percent = round((( free_mem / total_mem ) * 100),2)
        context = f"{used_mem} / {total_mem} ( {percent}% usage)"
        return context


    def screensize(self):
        import ctypes
        user32 = ctypes.windll.user32
        screen = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        screensize = f"{screen[0]}x{screen[1]} Pixels"

        return screensize



if platform.system() == "Linux":
    system = Linux()

elif platform.system() == "Windows":
    system = Windows()





#ClassBased Data:


#Real Time Information
screensize = system.screensize #win_screensize #screensize
tasks = system.process_counts #process_counts
uptime = system.uptime #uptime
battery_percent = system.battery_percentage
battery_runtime = system.battery_runtime

#Software Core/
kernel = system.kernel
os_version = system.os_name#os_versionr
build_version = system.build_version
processor_architecture = system.processor_architecture # processor_archi


terminal = system.terminal_name
shell = system.shell_name
desktop_manager = system.desktop_name


#HardwareBased informatin
gpu_name = system.gpu_name
cpu_name = system.cpu_name #f"{win_cpu()} @ { cpu_frequency[2]/100 } GHz "
cpu_frequency = lambda : (3000,3000,3000)
memory_info  = system.meminfo # meminfo


#Gloval Values


disk_information = disk_info




