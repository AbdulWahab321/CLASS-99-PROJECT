import os,shutil
BACKUP_FOLDER = r"D:\Backups"
if not os.path.exists(BACKUP_FOLDER):os.mkdir(BACKUP_FOLDER)
path = input("Path>> ")
if not os.path.exists(path):os.makedirs(path)
os.chdir(path)
for each in os.listdir(path):
    if os.path.isfile(each):
        if each.endswith(".png"):
            pngFolder = os.path.join(BACKUP_FOLDER,"PNG")
            if not os.path.exists(pngFolder):os.mkdir(pngFolder)
            shutil.copy(each,pngFolder)
        if each.endswith(".jpg"):
            jpgFolder = os.path.join(BACKUP_FOLDER,"JPG")
            if not os.path.exists(jpgFolder):os.mkdir(jpgFolder)
            shutil.copy(each,jpgFolder)
        if each.endswith(".jpeg"):
            jpegFolder = os.path.join(BACKUP_FOLDER,"JPEG")
            if not os.path.exists(jpegFolder):os.mkdir(jpegFolder)
            shutil.copy(each,jpegFolder)
        if each.endswith(".exe"):
            exeFolder = os.path.join(BACKUP_FOLDER,"EXE")
            if not os.path.exists(exeFolder):os.mkdir(exeFolder)
            shutil.copy(each,exeFolder)