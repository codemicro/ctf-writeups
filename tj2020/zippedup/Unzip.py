from zipfile import ZipFile
import tarfile
import os

folder = 0

maindir = "e:/CTFs/TJCTF/ZippedUp" # <-- This is the directory I used. You need to change it to yours

while True:
    os.chdir("e:/CTFs/TJCTF/ZippedUp/"+str(folder)) # <-- Same here
    things = os.listdir()
    for i in things:
        if i.endswith(".zip"):
            with ZipFile(i, 'r') as zipObj:
                zipObj.extractall(maindir)
        elif i.endswith(".bz2"):
            my_tar = tarfile.open(i)
            my_tar.extractall(maindir)
            my_tar.close()
        elif i.endswith(".kz3"):
            with ZipFile(i, 'r') as zipObj:
                zipObj.extractall(maindir)
        elif i.endswith(".gz"):
            my_tar = tarfile.open(i)
            my_tar.extractall(maindir)
            my_tar.close()
        else:
            continue
    os.chdir("..")
    folder += 1

        
