

def tst_middle_man(banner,data,limits,highest_key_len,seperator):
    #print(data,banner)
    
    #print(len(data))
    #pprint(data)
    index_keys = 0
    second_index_keys = 1


    #Avoid Error
    if len(data) < 7 :
        damn_len =  7 - len(data)
        darn = list(data.keys())[-1]
        
        for i in range(damn_len):
            #print(i)
            darn += 1 
            ind = darn
            data[ind] = ("","")




    #Detecting the highest len from from keys and values

    data_list = [( str(key) , str(val[0]+val[1]) ) for key,val in data.items() if key%2 == 0]
    lim = highest_middleman(data_list)




    #main work 

    limited_info_number = 17

    for ind,ban in enumerate(banner,3):

        if index_keys < limited_info_number :

            try :
       
                key = data[index_keys][0]
                val = data[index_keys][1]
        
                key2 = data[second_index_keys][0]
                val2 = data[second_index_keys][1]

            except :
                key = data[index_keys][0]
                val = data[index_keys][1]
                key2 = ""
                val2 = ""
    
            comb = str(key)+" "+str(val)

            seperator = " : "

            if (len(comb)+3) < lim:
                pass
                sep = " "* ( ( lim - len(str(key+val)) )+1 ) 
                print(key,seperator,val,sep,ban," ",key2,seperator,val2)


            else:
                if val2 == "":
                    seperator = "   "
                print(key,seperator,val,"  ",ban," ",key2,seperator,val2)

                seperator = " : "
            
            index_keys += 2
            second_index_keys +=2


        else:
            sep  = " "*(lim+8)
            print( sep,ban)
    
