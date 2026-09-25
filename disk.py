import psutil
from config_logges import logg



#print disk total

def get_disk_total ():
    disk =psutil.disk_usage('/')

    disk_total= disk.total / 1024 ** 3
    return '-' *65 ,f"the disk total is : {disk_total:.2f} GB " , '-' *65


#the gb in use (* 0.7 = total - 30%)max x{high}x

def get_disk_usage():
    disk =psutil.disk_usage('/')

    disk_usage = disk.used / 1024 ** 3
    disk_total= disk.total / 1024 ** 3

    if disk_usage <= disk_total * 0.7 :
         return "-" * 65 , f"the disk is : {disk_usage:.2f} GB" , "-" * 65
       
    else:
        message=f"the disk is nearly full : {disk_usage:.2f} GB"
        logg.warning(message)
        return "-" * 65 , message , "-" * 65


#the space free

def get_disk_free():
    disk =psutil.disk_usage('/')
    
    disk_free= disk.free / 1024 **3
    return "-" * 65 ,f"the free space is : {disk_free:.2f} GB " ,"-" * 65
    
