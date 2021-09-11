
from winfetch import __conf
from colorama import Fore

import os

os.system("cls")



#colors 
green = Fore.GREEN
cyan = Fore.CYAN
white = Fore.WHITE





def sort_it(datas):
	sorted_data = {}
	x = 0
	for key,value in datas.items():
		sorted_data[x] = (key,value)
		x+=1

	return sorted_data


def vartest(art):
	pass


def limit_determiner(banner):
    highest_val = 0 
    for line in banner:
        if len(line) > highest_val:
            highest_val = len(line)

    return highest_val



x = 0
info_dict = sort_it(__conf.sysfo)
banner = __conf.banner_name.split("\n")
limits = limit_determiner(banner)
whitespace = "    "
seperator = " : "


for i in range(len(banner)):


    try:
        #print(green ,banner[i], whitespace , cyan , key , seperator , white , value )
        key = info_dict[i][0]
        value= info_dict[i][1]

        if not len(banner[i]) < limits:
            #print(len(banner[i]))
            print(green ,banner[i], whitespace , cyan , key , seperator , white , value )
        else:
            print(" " * ( limits - len(banner[i]) ) , cyan, "      " , key , seperator , white,value)

    except KeyError:
        print(green,banner[i])
