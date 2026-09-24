
import psutil
from config_logges import logg


#RAM total ex:16GB

def get_ram_total() :
    ram=psutil.virtual_memory()
    ram_total= ram.total / 1024 ** 3
    return (f"the ram total is : {ram_total:.2f} GB")
    return get_ram_total




#RAM in uesd now



def get_ram_used():
    ram=psutil.virtual_memory()
    ram_total= ram.total / 1024 ** 3
    ram_used= ram.used / 1024 ** 3

    if ram_used <= ram_total *0.7 :
        return (f"the ram in uese is : {ram_used:.2f} GB")
       
    else:
       logg.warning(f"ram usage is high : {ram_used:.2f} GB")        

    return get_ram_used 

def call_all():
    print ('-' * 75) 
    get_ram_total()
    print ('-' * 75)
    get_ram_used()
    

