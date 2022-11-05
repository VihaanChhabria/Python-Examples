from serial import *
import serial.tools.list_ports
import pygame, time
from pygame.locals import *

ports = sorted(serial.tools.list_ports.comports())
i = 1
print("\n")
for elem in ports:
  print(i, " - " + elem[0])
  i = i + 1
selectedPort = input("Select COM port option: ")
comPort = ports[int(selectedPort) - 1][0]

serialPort = Serial(comPort, 9600, timeout=0, writeTimeout=0)

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Arduino Communication')

while 1:
  if serialPort.in_waiting:
    readLetter = serialPort.read()
    #print(readLetter)

  for event in pygame.event.get():
    if (event.type == KEYUP):
      serialPort.write(event.key)
      print(event.key)
         