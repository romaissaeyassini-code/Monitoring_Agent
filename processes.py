import psutil
from config_logges import logg



    #the head of the table 

def head():
    return  "-" * 65 ,f"{'PID':<8} {'NAME':<25} {'CPU%':<8} {'RAM%':<8} {'STATUS':<12}" , "-" * 65 , head
    
def get_process():
    processes = []
    
    for process in psutil.process_iter(
        ['pid', 'name', 'cpu_percent', 'memory_percent', 'status']
    ):
        try:
            info = process.info

            processes.append(
                        f"{info['pid']:<8} "
                        f"{info['name']:<13} "
                        f"{info['cpu_percent']:<5.1f} "
                        f"{info['memory_percent']:<8.2f} "
                        f"{info['status']:<12}"
                        )


        except psutil.NoSuchProcess as error1:
            logg.info(f"There is no such process: {error1}")
            return processes , error1 
        except psutil.AccessDenied as error2:
            logg.info(f"Access denied: {error2}")
            return processes ,error2 

        
       


        

 