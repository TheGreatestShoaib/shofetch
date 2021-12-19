

from subprocess import Popen, PIPE


def stdout_control(cmd):
	output = Popen(cmd,shell=True, stdout=PIPE).communicate()[0]
	return output.decode().strip()


TERMINAL = r"ps -aux | grep `ps -p $$ -o ppid=`" 
TERMINAL = "ps -p $$ -o ppid= | awk '{print $1}'"



process = stdout_control(TERMINAL)

print(process)

get_term  = "pstree -s "+process

term = stdout_control(get_term).split("---")
print(term)


input()
#print(stdout_control(TERMINAL))
