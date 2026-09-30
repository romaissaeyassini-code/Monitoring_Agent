from fastapi import FastAPI
from ram import get_ram_total , get_ram_used
from cpu import get_cpu_percent , get_cpu_count
from disk import get_disk_total , get_disk_usage , get_disk_free
from network import ping , tcp_ping
from processes import  head , get_process 
import database as db
import models 
from service import create_tables


# Crée les tables PostgreSQL
create_tables()


app = FastAPI()

@app.get("/Home")
def Welcom():
    return {"Welcome : Welcometo Process Monitor! "
            "Monitor your system processes in real time, check CPU and RAM usage, and easily identify which processes are consuming the most resources."}

@app.get("/Ram_Monitoring")
def ram():
    session = db.sessionlocal()

    try:#database= postgres
        used = get_ram_used()
        total = get_ram_total()

        data = models.RAM(
            ram_used=used,
            ram_total=total
        )

        session.add(data)
        session.commit()
        session.refresh(data)

        #aficher sur fatapi ui
        return {
            "The ID": data.id ,
            "The Ram in Used": f" {data.ram_used} GB",
            "The Ram Total": f"{data.ram_total} GB"
        } 

    except Exception: #Une erreur est arrivée → annule la transaction → puis montre-moi l'erreur
        session.rollback()
        raise

        # exécuté dans tous les cas.
    finally:
        session.close()



@app.get("/Cpu_Monitoring")
def cpu():

    session= db.sessionlocal()

    try:
        #pour postgres table
        percent= get_cpu_percent() 
        count_logical= get_cpu_count(logical=True) 
        count_pysical= get_cpu_count(logical=False) 

        data=models.CPU(
            percent= percent ,
            coures_logical= count_logical ,
            coures_pysical= count_pysical
        )

        session.add(data)
        session.commit()
        session.refresh(data)

        #pour fastapi

        return {
            "The ID" :data.id ,
            "The CPU Persent ":f"{data.percent} %" , 
            "The coures Logical ":f"{data.coures_logical} coures" ,
            "The Course Pysical ":f"{data.coures_pysical} coures"
        }
    except Exception:
        session.rollback()
        raise
    
        # exécuté dans tous les cas.
    finally:
        session.close()




@app.get('/Disk_Monitoring')
def disk():
    session = db.sessionlocal()

        #postgre table 
    try:
        total=get_disk_total()
        used=get_disk_usage()
        free=get_disk_free()

        data=models.Disk(
            disk_total=total,
            disk_used=used,
            disk_free=free )   

        session.add(data)
        session.commit()
        session.refresh(data)

            #fastapi
        return { 
        "The ID " :data.id ,
        "The Disk Total ": f"{data.disk_total} GB" ,
        "The Disk Used " : f"{data.disk_used} GB" ,
        "The Disk Free ": f"{data.disk_free} GB"
        }
     
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

    

@app.get("/PING/{host}")
def PING(host: str):
    return ping(host)

@app.get("/TCP_PING/{host}/{port}")
def TCP_PING(host:str , port:int):
    return f"the host: {host}" , f"the port : {port}" , tcp_ping(host,port)



@app.get('/process')
def process():
    return ( head (),get_process())
    





       




