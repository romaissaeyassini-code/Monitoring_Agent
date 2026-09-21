
import psutil
from config_logges import logg



    #the head of the table 

processes=[]

def get_process():
    print(f"{'PID':<8} {'NAME':<25} {'CPU%':<8} {'RAM%':<8} {'STATUS':<12}")
    print("-" * 65)

    for process in psutil.process_iter(
        ['pid', 'name', 'cpu_percent', 'memory_percent', 'status']
    ):
        #the and of the head
        # try to read and display the current process
        try:
            info = process.info
            print(
                f"{info['pid']:<8} "
                f"{info['name']:<25} "
                f"{info['cpu_percent']:<8.1f} "
                f"{info['memory_percent']:<8.2f} "
                f"{info['status']:<12}"
            )

        # Skip processes that disappear or cannot be accessed.
        except psutil.NoSuchProcess as error1:
            logg.info(f"ther is no such process : {error1}")

        except psutil.AccessDenied as error2:
            logg.info(f"ther access is denied : {error2}")


def call_all():
    print ('-' *75)
    get_process()

    print ('-' *75)
