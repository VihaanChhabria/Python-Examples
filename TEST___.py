from array import array
import socket
import time
import sys

import tk
import tkinter.simpledialog
root = tk()
root.withdraw()

PORT = 42001
HOST = tkinter.simpledialog.askstring('Scratch Connector', 'IP:')
if not HOST:
    sys.exit(1)

print ("Connecting...")
scratchSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
scratchSock.connect((HOST, PORT))
print ("Connected!")

def sendScratchCommand(cmd):
    n = len(cmd)
    a = array('c')
    a.append(chr((n >> 24) & 0xFF))
    a.append(chr((n >> 16) & 0xFF))
    a.append(chr((n >>  8) & 0xFF))
    a.append(chr(n & 0xFF))
    scratchSock.send(a.tostring() + cmd)

while True:
    msg = tkinter.simpledialog.askstring('Scratch Connector', 'Send Broadcast:')
    if msg:
        sendScratchCommand('broadcast "{}"'.format(msg))