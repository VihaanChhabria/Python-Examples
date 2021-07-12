import RPi.GPIO as GPIO
import time

run = True
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

while run == True:
    GPIO.output(11,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(11,GPIO.LOW)

    GPIO.output(12,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(12,GPIO.LOW)

    GPIO.output(15,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(15,GPIO.LOW)

    GPIO.output(16,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(16,GPIO.LOW)

    Hello = input("When Light Strikes Type l")

    if Hello == "l":
        print("You Got It!")