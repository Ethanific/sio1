# Exécuter en mode console
import os,time
from msvcrt import getch,kbhit

while True :
    if kbhit():
        z = getch() #lecture touche
        code  = ord(z) # code ASCII
        print (code)
        if code == ord('0'):
            os.system("cls")
    print('*')
    time.sleep(0.4)
