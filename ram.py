
import psutil
from config_logges import logg

ram=psutil.virtual_memory()
ram_total= ram.total / 1024 ** 3

#RAM total ex:16GB

def get_ram_total() :
    print (f"the ram total is : {ram_total:.2f} GB")

print ('-' * 75)
get_ram_total()


#RAM in uesd now

ram_used= ram.used / 1024 ** 3

def get_ram_used():

    if ram_used <= ram_total *0.7 :
        print (f"the ram in uese is : {ram_used:.2f} GB")
       
    else:
       logg.warning(f"ram usage is high : {ram_used:.2f} GB")        
         
        
print ('-' * 75)     
get_ram_used()


