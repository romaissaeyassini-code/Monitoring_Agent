from fastapi import FastAPI
from ram import get_ram_total , get_ram_used
from cpu import get_cpu_percent , get_cpu_count
from disk import get_disk_total , get_disk_usage , get_disk_free
from network import ping , tcp_ping
from processes import get_process 


app = FastAPI()

@app.get("/")
def meniu():
    return {"message": "Hello"}

@app.get("/test_ram")
def ram():
    return { get_ram_total() ,
             get_ram_used() 
            }

@app.get("/cpu")
def cpu():
    return {get_cpu_percent()  ,
            get_cpu_count(logical=True) , get_cpu_count(logical=False)
            }

@app.get('/disk')
def disk():
    return {get_disk_total() , get_disk_usage (), get_disk_free ()
    }

@app.get('/network')
def network ():
    return { ping() , tcp_ping ()}


@app.get('/process')
def process():
    return {"processes":get_process()}
    





       




