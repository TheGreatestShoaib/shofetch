
from colorama import Fore
from pprint import pprint








def gradient(banner,data,limits,highest_key_len):


    green = Fore.CYAN
    cyan = Fore.CYAN
    white = Fore.WHITE


    whitespace = "    "
    seperator = ":"

    half = len(banner)//2
    way_detector = 0

    for i in range(0,len(banner)):
        #print(i)
        try:
            if way_detector > half-1:
                green = Fore.BLUE

            key = data[i][0]
            value= data[i][1]

            if not len(banner[i]) < limits:

                if i == 1 :

                    print(green ,banner[i], whitespace , cyan , data[1] )
                
                elif i ==2 :
                    
                    print(green ,banner[i], whitespace , cyan , data[2] )

                else:

                    if len(key )< highest_key_len:
                        
                        key = key+ ( " " * ( highest_key_len - len(key) ) )
                        print(green ,banner[i], whitespace , cyan , key , seperator , white , value )
                    
                    else:
                        
                        print(green ,banner[i], whitespace , cyan , key , seperator , white , value )
            else:
                print(" " * ( limits - len(banner[i]) ) , cyan, "    " , key , seperator , white,value)
        
           





        

        except KeyError:
            print(green,banner[i])


        way_detector += 1


