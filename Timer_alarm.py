#A timer that can convert it self to hours minutes or AM to PM
import time
#from playsound import playsound

sec = 0
min = 0
hour = 0
am = True
pm = False
AMorPM = 1
nextday = 0
day = 0

while True:
    time.sleep(1)
    sec = sec + 1

    if sec == 60:
        min = min + 1
        sec = 0

    if min == 60:
        hour = hour + 1
        nextday = nextday + 1
        min = 0

    if hour == 13:
        hour = 1
        AMorPM = AMorPM * -1

    if AMorPM == 1:
        am = True
        pm = False

    if AMorPM == -1:
        am = False
        pm = True

    if nextday == 24:
        day = day + 1

    print(hour,":",min,":",sec)