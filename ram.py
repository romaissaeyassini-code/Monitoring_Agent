
import psutil
from config_logges import logg


#RAM total ex:16GB

def get_ram_total() :
    ram=psutil.virtual_memory()
    ram_total= ram.total / 1024 ** 3
    return  "-" * 65 ,f"the ram total is : {ram_total:.2f} GB" , "-" * 65

#RAM in uesd now


def get_ram_used():
    ram=psutil.virtual_memory()
    ram_total= ram.total / 1024 ** 3
    ram_used= ram.used / 1024 ** 3

    if ram_used <= ram_total *0.7 :
        return  "-" * 65 ,f"the ram in uese is : {ram_used:.2f} GB" , "-" * 65
       
    else:
       message=f"ram usage is high : {ram_used:.2f} GB"
       logg.warning(message)        

    return get_ram_used 


    

