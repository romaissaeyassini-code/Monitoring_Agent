import logging

# = basicConfig 

logg= logging.getLogger("logges")
logg.setLevel(logging.INFO)

format= logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
    )

#config de {v} file_handler /creat name/ mode= 'a' (append = in the end of the last line ) /format

file_Handler=logging.FileHandler(
    "logges.log" ,
     mode= "a"
     )

file_Handler.setFormatter(format)


#config console /creat/format

console_Handler= logging.StreamHandler()
console_Handler.setFormatter(format)

#send message to consol and file(logges.log)

logg.addHandler(file_Handler)
logg.addHandler(console_Handler)