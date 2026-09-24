import psutil
from config_logges import logg

    #the head of the table 

def get_process():
    process=[]
    print(f"{'PID':<8} {'NAME':<25} {'CPU%':<8} {'RAM%':<8} {'STATUS':<12}")
    print("-" * 65)

    for process in psutil.process_iter(
        ['pid', 'name', 'cpu_percent', 'memory_percent', 'status']
    ):

        #the and of the head


        #try= the table and 9iasat <8 8charakter in the left
        
        try:
            info = process.info

            print(
                f"{info['pid']:<8} "
                f"{info['name']:<25} "
                f"{info['cpu_percent']:<8.1f} "
                f"{info['memory_percent']:<8.2f} "
                f"{info['status']:<12}"
            )

        #2 type of erroe acces and no processes Pass to next peocess

        except psutil.NoSuchProcess as error1:

            logg.info(f"ther is no such process : {error1}")
            pass #not need it


        except psutil.AccessDenied as error2:
            
            logg.info(f"ther access is denied : {error2}")
            pass #not need it 

        return process
    return get_process
            

get_process()
print ('-' *75)




""" def get_processes():
    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "username", "cpu_percent", "memory_percent"]
    ):
        try:
            info = process.info

            processes.append({
                "pid": info["pid"],
                "name": info["name"],
                "username": info["username"],
                "cpu_percent": info["cpu_percent"],
                "memory_percent": round(info["memory_percent"], 2)
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return processes """