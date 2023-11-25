"""client.py 
### KHARI WALLACE, 100807131, TPRG 2131 ###

TPRG 2131 Fall 2023 Assignment 2
November 28th, 2023
Khari Wallace <khari.wallace@dcmail.ca>

# The client script establishes a connection to the Raspberry Pi monitoring server 
running on the Raspberry Pi.
"""


# Runs on Pc, directly from Thonny
# The client

import socket
s = socket.socket()
host = '192.168.4.43' # ip of raspberry pi, running the server
port = 5000
s.connect((host, port))
print(s.recv(1024))
s.close()
