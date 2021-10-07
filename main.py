
from winfetch import __conf
from colorama import Fore
import os , time , platform
from pprint import pprint


def clear():
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")

clear()

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


def limit_determiner(banner):
    highest_val = 0 
    for line in banner:
        if len(line) > highest_val:
            highest_val = len(line)

    return highest_val


def art_it(art):
	empt = []
	full = limit_determiner(art)
	count = 0
	for x in range(len(art)):
		if art[x] == ' ':
			print("bruh"+str(count))
		else:

			if len(art[x]) < full:
				mult = full - len(art[x])
				context = " "*mult
				empt.append(art[x]+context)
			count += 1
	return empt


info_dict = sort_it(__conf.sysfo)
raw_banner = __conf.banner_name.split("\n")
banner = art_it(raw_banner)
#banner = raw_banner






limits = limit_determiner(banner)
whitespace = "    "
seperator = " : "

half = len(banner)//2
way_detector = 0


for i in range(len(banner)):
    try:
        if way_detector > half:
            green = Fore.RED



        key = info_dict[i][0]
        value= info_dict[i][1]

        if not len(banner[i]) < limits:
            #print(len(banner[i]))
            print(green ,banner[i], whitespace , cyan , key , seperator , white , value )
        else:
            print(" " * ( limits - len(banner[i]) ) , cyan, "      " , key , seperator , white,value)
    
        way_detector += 1
    except KeyError:
        print(green,banner[i])


