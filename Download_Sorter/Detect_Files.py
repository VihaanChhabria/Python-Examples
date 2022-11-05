import glob
import shutil
import os
import keyboard

pic = [".gif", ".jpg", ".png", ".gifv", ".jfif"]
doc = [".doc", ".docx", ".odt", ".rtf", ".pdf", ".txt", ".epub"]
record = [".webm", ".mkv", ".flv", ".flv", ".vob", ".ogv", ".ogg", ".drc", ".gif", ".mng", ".avi", ".MTS", ".M2TS", ".TS", ".mov", ".qt", ".wmv", ".yuv", ".rm", ".rmvb", ".viv", ".asf", ".amv", ".mp4", ".m4p", ".m4v", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".mpg", ".mpeg", ".m2v", ".m4v", ".svi", ".3gp", ".3g2", ".mxf", ".roq", ".nsv", ".flv" ,".f4v" ,".f4p" ,".f4a" ,".f4b", ".wav"]

username = os.getlogin()

def move(username):
    download = "C:\\Users\\" + username + "\\Downloads\\*"
    move = "C:\\Users\\" + username + "\\Desktop\\Moved\\"

    for i in pic:
        #print(i)
        found = glob.glob(download + i)

        if found:
            move = move + "Pic"

            shutil.move(found[0], move)
            print("yes")

    for i in doc:
        #print(i)
        found = glob.glob(download + i)

        if found:
            move = move + "Doc"

            shutil.move(found[0], move)
            print("yes")

    for i in record:
        #print(i)
        found = glob.glob(download + i)

        if found:
            move = move + "Record"

            shutil.move(found[0], move)
            print("yes")

    found = glob.glob(download)

    if found:
        filename, file_extension = os.path.splitext(found[0])
        move = move + "Unknown"

        if not (file_extension in pic) and not (file_extension in doc) and not (file_extension in record):
            shutil.move(found[0], move)
            print("yes")

def init():
    if not glob.glob("C:\\Users\\" + username + "\\Desktop\\Moved\\Pic"):
        os.mkdir("C:\\Users\\" + username + "\\Desktop\\Moved\\Pic")

    if not glob.glob("C:\\Users\\" + username + "\\Desktop\\Moved\\Doc"):
        os.mkdir("C:\\Users\\" + username + "\\Desktop\\Moved\\Doc")

    if not glob.glob("C:\\Users\\" + username + "\\Desktop\\Moved\\Record"):
        os.mkdir("C:\\Users\\" + username + "\\Desktop\\Moved\\Record")

    if not glob.glob("C:\\Users\\" + username + "\\Desktop\\Moved\\Unknown"):
        os.mkdir("C:\\Users\\" + username + "\\Desktop\\Moved\\Unknown")

init()

while True:
    move(username)

    if (keyboard.read_key() == "ctrl") and (keyboard.read_key() == "shift"):
        os.system("start cmd /K cd C:\\Vihaan\\Python\\Scripts")
        break
        
    if keyboard.read_key() == "q":
        break
