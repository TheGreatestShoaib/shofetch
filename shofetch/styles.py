
from colorama import Fore
from pprint import pprint


def highest_middleman(dict_list):
    highest_val = 0

    for i in dict_list:
        combined_len = str(i[0]+i[1])
        if len(combined_len) >= highest_val:
            highest_val = len(combined_len)




    return highest_val





def gradient(banner,data,limits,highest_key_len,seperator):

    green = Fore.CYAN
    cyan = Fore.CYAN
    white = Fore.WHITE
    whitespace = "    "
    seperator = seperator

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






def tst_middle_man(banner,data,limits,highest_key_len,seperator):
    green = Fore.CYAN
    cyan = Fore.CYAN
    white = Fore.WHITE
    whitespace = "    "
    seperator = seperator

    half = len(banner)//2
    way_detector = 0


    print(len(banner))

    if len(banner) > len(data):
        b_dix = len(banner)
        f_bix = len(banner) // 2
    else:
        b_dix = len(data) // 2 

    print(b_dix)


    for i in range(b_dix):
        
        try :
            key = data[i][0]
            val = data[i][1]
            key2 = data[i+f_dix][0]
            val2 = data[i+f_dix][1]


            print(key,val,whitespace,banner[i],white,key2,val2)
        except Exception as e:
            
            print(key,":",val,whitespace,banner[i])
















def middle_man(banner,data,limits,highest_key_len,seperator):

    green = Fore.CYAN
    cyan = Fore.BLUE
    white = Fore.WHITE
    
    whitespace = "    "
    seperator = seperator
    half = len(banner)//2
    way_detector = 0
    lst = []

    
    key_list = [x for x in data.keys()]

    if (len(key_list) % 2) == 0:
        devision = len(key_list)//2
    else:
        devision = (len(key_list)//2)+1

    #devision = len(key_list)//2
    left_side_count = 1
    right_side_count = devision

    #print(right_side_count)
    
    minimal = (len(key_list)- right_side_count)+1

    ranged_sti_val = -2
    ranged_eti_val = right_side_count-1

    ranged_sti_val = -2
    ranged_eti_val = right_side_count-1

    for i in range(ranged_sti_val,ranged_eti_val):
        try:
            
            data_key = data[i+2][0]
            data_value = data[i+2][1]
            
            lst.append( (data_key,data_value) )
        
        except KeyError:
            pass


    #print(len(lst))

    lim = highest_middleman(lst)
    

    i=0

    while left_side_count < minimal:

        right_side_count = i+minimal


        try:
            #apply gradient effect by changing color here

            if way_detector > half-1:
                cyan = Fore.RED


            #defing data for both sides

            key=data[left_side_count][0]
            key_2 = data[right_side_count][0]
            
            value = data[left_side_count][1]
            value_2 = data[right_side_count][1]
            
            combined_len = str(key+value)


            #main theme starts here
            
            if len(combined_len) <= lim:
                sep = " "*((lim-len(combined_len))+1) 
                print(green ,key,seperator,value,sep, cyan, banner[i],"   ",green ,key_2,seperator,value_2)

            else:
                print(green ,key,seperator,value, cyan, banner[i], green ,key_2,seperator,value_2)

        except:

            combined_len = str(key+value)
            if len(combined_len) <= lim:
                sep = " "*((lim-len(combined_len))+1) 
                print(green ,key,seperator,value,sep, cyan, banner[i])  

            else:
                print(green ,key,seperator,value, cyan, banner[i])

        
        #increment Vars
        i+=1
        left_side_count+=1
        right_side_count+=1
        way_detector+=1
