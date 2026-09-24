import subprocess 
import socket
from config_logges import logg


#ping sur host 


def ping(host: str):
    result = subprocess.run(
        ["ping", "-n", "1", host],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return {
            "host": host,
            "success": True,
            "result": result.stdout
        }

    else:
        message = f"Ping request could not find host {host}. Please check the name and try again"

        logg.info(message)

        return {
            "host": host,
            "success": False,
            "result": message
        }


#tcp ping 


def tcp_ping(host:str , port:int):


    try:
            #Connect to address and return the socket. Connect to address (host, port)

        socket.create_connection((host , port) , timeout=3)
        message= f"port is connected : {host}:{port}"
        logg.info (message)
        return message 
                  
    except (socket.timeout,OSError):
            
            message1=  f"TCP connection failed : {host}:{port}","tcheck the host name or the port "
            logg.warning(message1)
            return message1 
    





