import psutil
from config_logges import logg


try:
    p=psutil.Process(9999999)
    print (p.name())

except psutil.NoSuchProcess as e:
    logg.info(f"the is no such process : {e}")
    