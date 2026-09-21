import psutil
from config_logges import logg


cpu= psutil.cpu_percent (interval=1)

#cpu persent % / warning 

def get_cpu_percent():    
    if cpu <= 75 :
       print (f"the cpu percent is : {cpu}  %")

    else:
       logg.warning(f"the cpu percent is high : {cpu}  %")
       
       
print ('-' * 75)
get_cpu_percent()

#cpu cour logical & physique 

def get_cpu_count(logical=False):
    cpu_count= psutil.cpu_count(logical=logical)

    if logical :
     print (f'the nomber of cpu cour logical is  : {cpu_count} cour')
    else:
        print (f'the nomber of cpu cour physique is  : {cpu_count} cour')


print ('-' * 75)

get_cpu_count(False)
get_cpu_count(True)



