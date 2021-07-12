#Using a rasberry pi it will turn on a light
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('TRAP TRIGGERD')
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.2)
