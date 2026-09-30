
import psutil
from config_logges import logg


#RAM total ex:16GB

def get_ram_total() :
    ram=psutil.virtual_memory()
    
    return round(ram.total / (1024 ** 3), 2)

#RAM in uesd now


def get_ram_used():
    ram=psutil.virtual_memory()
    ram_total= ram.total / 1024 ** 3
    ram_used= ram.used / 1024 ** 3

    if ram_used <= ram_total *0.7 :
        return  round(ram_used,2)
       
    else:
        message = f"RAM usage is high: {ram_used:.2f} GB"
        logg.warning(message)

        return round(ram_used, 2)


    

