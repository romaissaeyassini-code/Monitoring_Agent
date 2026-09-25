import subprocess 
import socket
from config_logges import logg


#ping sur host 

def ping():
    host = input("Enter host: ")
    
    #exiqute les command windows = ipconfig /linux '-c'/'-n'win /

    result=subprocess.run(
        ["ping", "-n", "1", host],

        capture_output= True,
        text=True

        )
                    #stdout=le resulta de ping selment
    if result.returncode == 0:
        print(f"{result.stdout}")

    else :
        logg.info(f"Ping request could not find host  {host} . Please check the name and try again")         



#tcp ping 


def tcp_ping():
    print ("test la connetiveite sur tcp ")

    host = input("Enter host: ")
    port=(input("entre le port : "))


    try:
            #Connect to address and return the socket. Connect to address (host, port)

            socket.create_connection((host , port) , timeout=3)

            logg.info (f"port is connected : {host}:{port}")
            return True
                  
    except (socket.timeout,OSError,ValueError):
            logg.info(f"Error: the port must be a number : {ValueError}") 
            logg.warning( f"TCP connection failed : {host}:{port} ")
            return False


def call_all():
    print('-' * 75) 
    ping()
    print('-' * 75)       
    tcp_ping()
    print('-' * 75)


