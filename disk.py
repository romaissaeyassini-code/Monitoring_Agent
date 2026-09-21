import psutil
from config_logges import logg

disk =psutil.disk_usage('/')

disk_total= disk.total / 1024 ** 3


#print disk total

def get_disk_total ():
    print (f"the disk total is : {disk_total:.2f} GB ")


print ('-' *70)
get_disk_total()


#the gb in use (* 0.7 = total - 30%)max x{high}x

disk_usage = disk.used / 1024 ** 3

def get_disk_usage():

    if disk_usage <= disk_total * 0.7 :
         print(f"the disk is : {disk_usage:.2f} GB")
       
    else:
        logg.warning(f"the disk is nearly full : {disk_usage:.2f} GB")
        
        
print ('-' *70)
get_disk_usage()


#the space free

def get_disk_free():

    disk_free= disk.free / 1024 **3
    print (f"the free space is : {disk_free:.2f} GB ")


print ('-' *70)
get_disk_free()


