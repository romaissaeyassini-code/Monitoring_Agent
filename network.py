import subprocess 
import socket
from config_logges import logg


print('-' * 100)
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

print('-' * 100)
ping()
print('-' * 100)



#tcp ping 

print ("test la connetiveite sur tcp ")

def tcp_ping():

    host = input("Enter host: ")
    port=int(input("entre le port : "))

    try:
            #Connect to address and return the socket. Connect to address (host, port)

            socket.create_connection((host , port) , timeout=3)

            logg.info (f"port is connected : {host}:{port}")
            return True
                  
    except (socket.timeout,OSError):
            
            logg.warning( f"TCP connection failed : {host}:{port} ")
            return False


print('-' * 100)
tcp_ping()
print('-' * 100)