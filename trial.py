

import winfetch_core as winf 
from pprint import pprint




def sort_it(datas):
	sorted_data = {}
	x = 0
	for key,value in datas.items():
		sorted_data[x] = (key,value)
		x+=1

	return sorted_data


hello = sort_it(winf.sysfo)

pprint(hello)

print(winf.logo.windows)


print(winf.logo.__LOGOS__)