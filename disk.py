import psutil
from config_logges import logg



#print disk total

def get_disk_total ():
    disk =psutil.disk_usage('/')
    return round (disk.total / (1024 ** 3),2)


#the gb in use (* 0.7 = total - 30%)max x{high}x

def get_disk_usage():
    disk =psutil.disk_usage('/')

    disk_usage = disk.used / 1024 ** 3
    disk_total= disk.total / 1024 ** 3

    if disk_usage <= disk_total * 0.7 :
         return round(disk_usage ,2)
       
    else:
        message=f"the disk is nearly full : {disk_usage:.2f} GB"
        logg.warning(message)
        return round(disk_usage ,2)


#the space free

def get_disk_free():
    disk =psutil.disk_usage('/')
    return round(disk.free / (1024 **3) ,2)
    
