import psutil
from config_logges import logg


#cpu persent % / warning 

def get_cpu_percent(): 
    cpu= psutil.cpu_percent (interval=1)   
    if cpu <= 75 :
       return cpu
       
    else:
       message=f"the cpu percent is high : {cpu}  %"
       logg.warning(message)
       return cpu
    


#cpu cour logical & physique 

def get_cpu_count(logical=False):
    cpu_count= psutil.cpu_count(logical=logical)

    if logical :
     return cpu_count
     
    else:
        return cpu_count
    



