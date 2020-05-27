import shutil
import os

maindir = "e:/CTFs/TJCTF/ZippedUp/Flags" # <-- This is the directory I used. You need to change it to yours
folder = 1

for i in range(1001):
    shutil.copy(maindir+"/"+str(folder)+"/"+str(folder)+".txt", maindir) # <-- Same here
    folder += 1
    i += 1
