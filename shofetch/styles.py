
from colorama import Fore
from pprint import pprint


def highest_middleman(dict_list):
    highest_val = 0

    for i in dict_list:
        combined_len = str(i[0]+i[1])
        if len(combined_len) >= highest_val:
            highest_val = len(combined_len)

    return highest_val

def max_valer(dset1,dset2,ban):

    dlen1 = len(dset1)
    lenban = len(ban)
    dlen2 = len(dset2)

    # checks if both datasets are same
    if dlen1 == dlen2 :
        #if both datasets and the banner is same
        if lenban == dlen1 :
            lst = [ dset1 ,dset2 , ban ]
            return lst
        

        elif lenban > dlen1 :
            # if banner is bigger than data then add false data

            for i in range(lenban-dlen1):
                dset1.append(("",""))
                dset2.append(("",""))
                
            
            lst = [ dset1 ,dset2 , ban ]
            return lst
        
        elif lenban < dlen1:
            
            # if banner is smaller than data then add false banner
            ban.append(("",""))
            lst = [ dset1 ,dset2 , ban ]
            return lst


    elif dlen1 != dlen2:
        if dlen1 < dlen2 :
            dset1.append(("",""))
            return max_valer(dset1 ,dset2 , ban)
        if dlen1 > dlen2 :
            dset2.append(("",""))
            return max_valer(dset1 ,dset2 , ban)







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


    #Constant Values
    whitespace = "     "

    rawlen = len(data)
    datalen = len(data) // 2

    #Manipulted Datas
    fst = [data[i] for i in range(datalen+1)]
    snd = [data[i] for i in range(rawlen - datalen,rawlen)]

    #wrapper funcs 
    last_result = max_valer(fst,snd,banner)
    high = highest_middleman(fst)+2

    # Loops Printer
    for l in range(len(last_result[2])):
        
        #checks None type and fixes first columns structure
        if last_result[0][l][0] != "":
            damn = last_result[0][l][0]+ " : " +last_result[0][l][1] 
        else :
            damn = ""

        #checks None type and fixed third Columns structure

        if last_result[1][l][0] != "":
            lastcol = last_result[1][l][0] + " : " + last_result[1][l][1]
        else :
            lastcol = ""


        #Main printing parts 
        if len(damn) <= high: 
            print(damn," "*(high-len(damn)) ,whitespace ,last_result[2][l] ,whitespace , lastcol )
        else:
            print(damn,whitespace ,last_result[2][l] ,whitespace ,lastcol  )




