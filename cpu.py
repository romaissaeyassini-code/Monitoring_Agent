import psutil
from config_logges import logg


#cpu persent % / warning 

def get_cpu_percent(): 
    cpu= psutil.cpu_percent (interval=1)   
    if cpu <= 75 :
       return "-" * 65 , f"the cpu percent is : {cpu}  %" , "-" * 65
       

    else:
       message=f"the cpu percent is high : {cpu}  %"
       logg.warning(message)
       return "-" * 65 , message , "-" * 65
    


#cpu cour logical & physique 

def get_cpu_count(logical=False):
    cpu_count= psutil.cpu_count(logical=logical)

    if logical :
     return  "-" * 65 , f'the nomber of cpu cour logical is  : {cpu_count} cour' , "-" * 65
     
    else:
        return  "-" * 65 , f'the nomber of cpu cour physique is  : {cpu_count} cour', "-" * 65
    
        
    



def call_all():
    print ('-' * 75)
    get_cpu_percent()
    get_cpu_count(False)
    get_cpu_count(True)
    print ('-' * 75)



