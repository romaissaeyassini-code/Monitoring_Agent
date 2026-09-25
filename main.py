import psutil
from config_logges import logg
import cpu
import ram
import disk
import network
import processes 


def main():
        
        print("SERVER MONITORING SYSTEM  : \n"
            "1. CPU Monitoring \n"
            "2. RAM Monitoring\n"
            "3. Disk Monitoring \n"
            "4. Network Monitoring\n" 
            "5. Processes Monitoring \n"
        )

        meniu=int(input("chose un nomber :"))

        if meniu == 1:
            cpu.call_all() 

        if meniu == 2:
            ram.call_all()

        if meniu == 3:
            disk.call_all()

        if meniu == 4:
             network.call_all()

        if meniu == 5:
             processes.call_all()


main()