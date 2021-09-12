
from pprint import pprint
from subprocess import Popen, PIPE



WIN_GPU = "powershell \"Get-CimInstance -ClassName Win32_VideoController -Property caption|Select-Object caption \"" 
WIN_GPU = "wmic cpu get name,Threadcount"






def get_gpu():
	output = Popen(WIN_GPU,shell=True, stdout=PIPE).communicate()[0].decode().split("\n")
	return output






bruh = get_gpu()

for i in bruh:
	pprint(i)