import time
from pprint import pprint
start =  time.perf_counter()

from shofetch import __conf
from colorama import Fore
import os, platform
from pprint import pprint
#import styles
import emojis

from shofetch import styles











# CONFIG_DATA = __conf.confs_getter()

CONFIG_DATA = __conf.sysfo

# pprint(CONFIG_DATA)

def clear():
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")

clear()


def clean_it(dict):
    
    new_dict = {}

    for i,j in dict.items():
        if j[1] != "" and j[1] != "None" and j[1] is not None:
            new_dict[i] = j

    return new_dict



#colors 
green = Fore.GREEN
cyan = Fore.CYAN
white = Fore.WHITE

def sort_it(datas,sort_system = __conf.theme):

	if platform.system()== "Linux":
		user = os.environ["USER"]
	else:
		user = os.environ["USERNAME"]	

	sorted_data = {}

	if sort_system == "default":
		sorted_data[1] = f'{user}@{platform.uname().node} '
		sorted_data[2] = '--------------'
		x = 3

	else:
		x = 0

	for key,value in datas.items():
		# if key is not None and value is not None:
		sorted_data[x] = (key,value)
		# else:
		# pass
		x+=1

	return sorted_data




def highest_keylen(data):

	highest = 0 

	for key in data.values():
		if len(key[0]) > highest:
			highest = len(key[0])
			#print(highest,key[0])

	return highest



def limit_determiner(banner):
    highest_val = 0 
    for line in banner:
        if len(line) > highest_val:
            highest_val = len(line)

    return highest_val

def art_it(art):
	empt = []
	full = limit_determiner(art)
	for x in range(len(art)):
		if art[x] == ' ':
			pass
		else:

			if len(art[x]) < full:
				mult = full - len(art[x])
				context = " "*mult
				empt.append(art[x]+context)
			else:
				empt.append(art[x])
	return empt

def defult_msg():
    whitespace=" "*31
    print(whitespace,end='')
    for i in range(31,35):
        color = f"\033[1;{i}m "
        print(color,red,end='')

    print()
    print(whitespace,end='')
    for i in range(36,40):
        color = f"\033[1;{i}m "
        print(color,red,end='')



def chinese_msg():
    word = [36781,36782 ,36783 ,36784 ,36785 ,36786]
    whitespace = " "*29
    x = 0
    print(whitespace,end="")
    for i in range(31,35):

        print(f"\033[1;{i}m",chr(word[x]),end="")
        x+=1
    x=0
    for i in range(31,35):
        print(f"\033[1;{i}m",chr(word[x]),end="")
        x+=1


# def custom_msg():
#     whitespace = "                       "
#
#     word = "devoured by her smile and now suffocating for her stupidity"
#
#
#     i = 31
#     x = 0
#     print(whitespace,end="")
#     while x < len(word):
#         color = f"\033[1;{i}m"
#         print(color+word[x],end="")
#         x+=1
#         if i > 37:
#             i=31
#
#         i+=1

def custom_msg(msg, whitespace_multiplier):
    whitespace = " " * whitespace_multiplier

    print()
    # word = "وَهُوَ  بِكُلِّ  شَيْءٍ  عَلِيمٌ"[::-1]
    # word = "ﻻ ﺗَﻘْﻨَﻄُﻮﺍ ﻣِﻦ ﺭَّﺣْﻤَﺔِ ﺍﻟﻠَّﻪِ"[::-1]
    # word  = 'لَا تَقْنَطُوا مِنْ رَحْمَةِ اللَّهِ' [::-1]
    # #word = "رَبَّنَا ظَلَمْنَا أَنفُسَنَا وَإِن لَّمْ تَغْفِرْ لَنَا وَتَرْحَمْنَا لَنَكُونَنَّ مِنَ الْخَاسِرِينَ"[::-1]
    # word = "اَللَّهُمَّ أَجِرْنِي مِنَ النَّارِ"[::-1]
    # word = "U+0628U+0650U+0643U+064FU+0644U+0650U+0651 U+0634U+064EU+064AU+0652U+0621U+064D U+0639U+064EU+0644U+0650U+064AU+0645U+064C"
    #word = chr(word)
    word = msg
    i = 31
    x = 0
    print(whitespace,end="")
    while x < len(word):
        color = f"\033[1;{i}m"
        print(color+word[x],end="",flush=True)
        time.sleep(0.008)
        x+=1
        if i > 37:
            i=31

        i+=1
    print()





if __name__ == "__main__":



	info_dict = sort_it(CONFIG_DATA)
	raw_banner = __conf.banner_name.split("\n")
	banner = art_it(raw_banner)
	#banner = raw_banner

	limits = limit_determiner(banner)
	# whitespace = "    "
	# seperator = " : "

	# half = len(banner)//2
	# way_detector = 0
	#print(info_dict)

	# keylen= highest_keylen(info_dict)
	keylen = 10
	
	if __conf.theme == "default":
		styles.gradient(banner,info_dict,limits,keylen,":")
	elif __conf.theme == "midway":
		styles.tst_middle_man(banner,info_dict,limits,keylen,":")

	
	red = emojis.encode(':yellow_circle:')




	if __conf.msg_type == "chinese":
		chinese_msg()

	elif __conf.msg_type == "custom":
		custom_msg(__conf.custom_msg_txt,(int(len(banner[-1])) + __conf.custom_msg_padding ))
	elif __conf.msg_type == "None" :
		print()
	else:
		defult_msg()

