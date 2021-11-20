
from shofetch import __conf
from colorama import Fore
import os , time , platform
from pprint import pprint
#import styles
import emojis

from shofetch import styles



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

def sort_it(datas,sort_system = "midway"):

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



	#1: f'{user}@{platform.uname().node} ',
	#2:'--------------',
	#}
	

	for key,value in datas.items():
		sorted_data[x] = (key,value)
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
    whitespace="                     "
    print(whitespace,end='')
    for i in range(31,35):
        color = f"\033[1;{i}m "
        print(color,red,end='')

    print()
    print(whitespace,end='')
    for i in range(36,39):
        color = f"\033[1;{i}m "
        print(color,red,end='')



def chinese_msg():
    word = [36781,36782 ,36783 ,36784 ,36785 ,36786]
    whitespace = "                      "
    x = 0
    print(whitespace,end="")
    for i in range(31,35):

        print(f"\033[1;{i}m",chr(word[x]),end="")
        x+=1
    x=0
    for i in range(31,35):
        print(f"\033[1;{i}m",chr(word[x]),end="")
        x+=1


def custom_msg():
    whitespace = "                       "

    word = "devoured by her smile and now suffocating for her stupidity"


    i = 31
    x = 0
    print(whitespace,end="")
    while x < len(word):
        color = f"\033[1;{i}m"
        print(color+word[x],end="")
        x+=1
        if i > 37:
            i=31

        i+=1

def custom_msg():
    whitespace = "                       "

    #word = "devoured by her smile and now suffocating for her stupidity"
    print()
    word = "وَهُوَ  بِكُلِّ  شَيْءٍ  عَلِيمٌ"[::-1]

    word = "ﻻ ﺗَﻘْﻨَﻄُﻮﺍ ﻣِﻦ ﺭَّﺣْﻤَﺔِ ﺍﻟﻠَّﻪِ"[::-1]
    word  = 'لَا تَقْنَطُوا مِنْ رَحْمَةِ اللَّهِ' [::-1]
    #word = "رَبَّنَا ظَلَمْنَا أَنفُسَنَا وَإِن لَّمْ تَغْفِرْ لَنَا وَتَرْحَمْنَا لَنَكُونَنَّ مِنَ الْخَاسِرِينَ"[::-1]


    #word = "اَللَّهُمَّ أَجِرْنِي مِنَ النَّارِ"[::-1]
    #word = "U+0648U+064EU+0647U+064FU+0648U+064E U+0628U+0650U+0643U+064FU+0644U+0650U+0651 U+0634U+064EU+064AU+0652U+0621U+064D U+0639U+064EU+0644U+0650U+064AU+0645U+064C"
    #word = chr(word)

    i = 31
    x = 0
    print(whitespace,end="")
    while x < len(word):
        color = f"\033[1;{i}m"
        print(color+word[x],end="")
        x+=1
        if i > 37:
            i=31

        i+=1



if __name__ == "__main__":


	info_dict = sort_it(__conf.sysfo)
	raw_banner = __conf.banner_name.split("\n")
	banner = art_it(raw_banner)
	#banner = raw_banner

	limits = limit_determiner(banner)
	# whitespace = "    "
	# seperator = " : "

	# half = len(banner)//2
	# way_detector = 0
	#print(info_dict)

	keylen= highest_keylen(info_dict)
	print()
	
	if __conf.theme == "default":
		styles.gradient(banner,info_dict,limits,keylen,":")
	elif __conf.theme == "midway":
		styles.tst_middle_man(banner,info_dict,limits,keylen,":")

	
	red = emojis.encode(':yellow_circle:')


	print()



	if __conf.msg_type == "chinese":
		chinese_msg()

	elif __conf.msg_type == "custom":
		custom_msg()
	else:
		defult_msg()



print()
print()

