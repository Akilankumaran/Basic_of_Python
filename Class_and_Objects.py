class laptop:
    Price = ""
    Processor = ""
    ram = ""
HP = laptop()
DELL = laptop()
LENOVO = laptop()    

HP.Price = 5000 
HP.Processor = "i3"
HP.ram = "8gb"

DELL.Price = 10000  
DELL.Processor = "i5"
DELL.ram = "8gb"

LENOVO.Price = 20000
LENOVO.Processor = "16gb"
LENOVO.ram = "32gb"

print(HP.Price, HP.Processor, HP.ram)
