import psutil
from config_logges import logg


#cpu persent % / warning 

def get_cpu_percent(): 
    cpu= psutil.cpu_percent (interval=1)   
    if cpu <= 75 :
       return (f"the cpu percent is : {cpu}  %")
       

    else:
       logg.warning(f"the cpu percent is high : {cpu}  %")
       return f"the cpu percent is high : {cpu}  %"
    return get_cpu_percent()


#cpu cour logical & physique 

def get_cpu_count(logical=False):
    cpu_count= psutil.cpu_count(logical=logical)

    if logical :
     return (f'the nomber of cpu cour logical is  : {cpu_count} cour')
     
    else:
        return (f'the nomber of cpu cour physique is  : {cpu_count} cour')
    
    return get_cpu_count()    
    



def call_all():
    print ('-' * 75)
    get_cpu_percent()
    get_cpu_count(False)
    get_cpu_count(True)
    print ('-' * 75)



