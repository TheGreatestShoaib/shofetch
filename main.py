
from winfetch import __conf
from colorama import Fore
import os , time , platform
from pprint import pprint
import styles
import emojis




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
	sorted_data = {
	1: f'{os.environ["USER"]}@{platform.uname().node} ',
	2:'--------------',

	}
	x = 3
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


info_dict = sort_it(__conf.sysfo)
raw_banner = __conf.banner_name.split("\n")
banner = art_it(raw_banner)
#banner = raw_banner






limits = limit_determiner(banner)
# whitespace = "    "
# seperator = " : "

# half = len(banner)//2
# way_detector = 0



keylen= highest_keylen(info_dict)


styles.gradient(banner,info_dict,limits,keylen)

red = emojis.encode(':yellow_circle:')


print()


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





if __conf.msg_type == "chinese":
    chinese_msg()

elif __conf.msg_type == "custom":
    custom_msg()
else:
    defult_msg()





# for i in range(len(banner)):
#     try:
#         if way_detector > half:
#             green = Fore.RED



#         key = info_dict[i][0]
#         value= info_dict[i][1]

#         if not len(banner[i]) < limits:
#             #print(len(banner[i]))
#             print(green ,banner[i], whitespace , cyan , key , seperator , white , value )
#         else:
#             print(" " * ( limits - len(banner[i]) ) , cyan, " " , key , seperator , white,value)
    
#         way_detector += 1
#     except KeyError:
#         print(green,banner[i])

print()
print()
