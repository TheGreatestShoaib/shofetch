



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


