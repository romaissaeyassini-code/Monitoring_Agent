from fastapi import FastAPI

import psutil
from config_logges import logg
from cpu import call_all




app=FastAPI()

@app.get("/cpu")
def call_all():
    cpu_percent = psutil.cpu_percent()
    physical = psutil.cpu_count(logical=False)
    logical = psutil.cpu_count(logical=True)

    return {
        "cpu_percent": cpu_percent,
        "physical_cores": physical,
        "logical_cores": logical
    }







    """ return ram.call_all()

    return disk.call_all()

    return network.call_all()

    return processes.call_all() """
             


