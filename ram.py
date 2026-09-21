
import psutil
from config_logges import logg


#RAM total ex:16GB

def get_ram_total() :
    ram=psutil.virtual_memory()
    ram_total= ram.total / 1024 ** 3
    print (f"the ram total is : {ram_total:.2f} GB")



#RAM in uesd now



def get_ram_used():
    ram=psutil.virtual_memory()
    ram_total= ram.total / 1024 ** 3
    ram_used= ram.used / 1024 ** 3

    if ram_used <= ram_total *0.7 :
        print (f"the ram in uese is : {ram_used:.2f} GB")
       
    else:
       logg.warning(f"ram usage is high : {ram_used:.2f} GB")        
         

def call_all():
    print ('-' * 75) 
    get_ram_total()
    print ('-' * 75)
    get_ram_used()


