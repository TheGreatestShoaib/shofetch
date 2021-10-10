


with open('sites.txt', 'r') as f:
    for line in f.readlines():
        if line.startswith('https://') or line.startswith('http://'):
        	hello = line.split('/')
        	print(hello[2])

