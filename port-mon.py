import socket
import time
import datetime

ip = '10.77.200.126'
port_tcp = 1433
counter_dead = 0
counter_alive = 0

def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False

while True:
    status = ""
    
    if isOpen(ip, port_tcp):
        status = "Ok"
        counter_alive += 1
    else:
        status = "Dead"
        counter_dead += 1
    
    print(str(datetime.datetime.now().time()) 
    + " -> Connect check: "
    + str(ip)
    + " Status: " + status
    + " Fail: " 
    + str(counter_dead) 
    + " Ok: "
    + str(counter_alive))
    time.sleep(1)
