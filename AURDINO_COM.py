import serial
import time
import keyboard

arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    p = keyboard.read_key()

    if p == "w":
        value = write_read("1")

    elif p == "a":
        value = write_read("2")

    elif p == "s":
        value = write_read("3")

    elif p == "d":
        value = write_read("4")

    elif p == "A":
        value = write_read("5")

    elif p == "D":
        value = write_read("6")
    else:
        value = write_read("0")