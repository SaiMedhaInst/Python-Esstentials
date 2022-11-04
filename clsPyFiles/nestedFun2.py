def print_msg(msg):
    def printer(name): 
        return msg+" "+name
    
    a=printer("Python")
    print(a)
    a+= " Lang"
    return a

res = print_msg("Hello")
print(res)