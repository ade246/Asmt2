"""server.py 
### KHARI WALLACE, 100807131, TPRG 2131 ###

TPRG 2131 Fall 2023 Assignment 2
November 28th, 2023
Khari Wallace <khari.wallace@dcmail.ca>

# This server runs on Pi, sends the Pi's 4 arguments from the vcgencmds,
sent as Json object.
"""

import socket
import os, time
import json

s = socket.socket()
host = '' # Localhost
port = 5000
s.bind((host, port))
s.listen(5)

# Function to get Core Temperature from Pi
def get_core_temperature():
    temperature = os.popen('vcgencmd measure_temp').readline()
    return temperature.strip()

# Function to get CPU Clock Frequency from Pi
def get_cpu_clock_frequency():
    frequency = os.popen('vcgencmd measure_clock arm').readline()
    return frequency.strip()

# Function to get GPU Memory Usage from Pi
def get_gpu_memory_usage():
    memory_usage = os.popen('vcgencmd get_mem reloc').readline()
    return memory_usage.strip()



while True:
  c, addr = s.accept()
  print ('Got connection from',addr)
  res = bytes(str(f_dict), 'utf-8') # needs to be a byte
  c.send(res) # sends data as a byte type
  c.close()