

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;12;25;155m".format(r, g, b, text)
  
text = 'Hello, World'
colored_text = colored(255, 0, 0, text)
print(colored_text)

#or

print(colored(255, 0, 0, 'Hello, World'))


