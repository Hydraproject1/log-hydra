#Directed By Hydra_project in 23/01/2019
from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           print('       \033[1;36;40m<─────────────── Hydra ───────────────>')
           print('')
           os.system('date | lolcat')
           print("\033[1;93m")
           print(" \033[1;92m                 Termux Locked By Hydra")
           print("\033[1;93m")
           print("         <───────[ Log in your Termux ]───────>")
           print("")
           try:
                user = str(input('\033[1;92mUsername \033[1;93m: '))
                print("")
                password = getpass('\033[1;92mPassword \033[1;93m: ')
                print ("")
                if user=="hydra" and password=="hydra":
                   print('wait...')
                   time.sleep(1)
                   os.system('clear')
                   print('')
                   os.system('figlet ' + user + ' | lolcat')
                   print('\033[1;92m ────────────────────────────────────── ')
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)
                      print("")
           except Exception:
                      
                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)
menu()
