import os
import time
import struct
import pyaudio
import win32api
import Fortuna

#https://www.scopus.com/record/display.uri?eid=2-s2.0-70449470310&origin=resultslist&sort=plf-f&src=s&sid=db4296379cd4a73544e78d5087326eb2&sot=b&sdt=b&s=TITLE-ABS-KEY%28True+random+number+generators+on+PC%29&sl=45&sessionSearchId=db4296379cd4a73544e78d5087326eb2
#https://github.com/otms61/fortuna


def mic_entropy(blocksize):
    # Open a PyAudio stream to capture microphone input
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=blocksize)
    # Read a block of samples from the stream
    block = stream.read(blocksize)
    # Convert samples to integers and pack into a bytes object
    data = struct.pack('<' + str(blocksize//2) + 'h', *struct.unpack('<' + str(blocksize//2) + 'h', block))
    # Return the bytes object as entropy
    return data

def mouse_entropy(blocksize):
    # Read a block of mouse events
    events = []
    t = time.time()
    while time.time() - t < 1:
        # Read a single mouse event
        data = win32api.GetCursorPos()
        events.append((data[0], data[1]))
        # Sleep briefly to avoid hogging the CPU
        time.sleep(0.001)
    # Pack the event data into a bytes object
    data = struct.pack('<' + str(blocksize) + 'I', *events)
    # Return the bytes object as entropy
    return data

def network_entropy(blocksize):
    # TODO: Implement network entropy source
    return b''

def trng(length):
    
    return 

# Generate 10 decimal numbers from the TRNG and write them to a file
with open('trng_decimals.txt', 'w') as f:
    bytes_per_decimal = 4 # We'll use 4 bytes per decimal number
    for i in range(10):
        # Generate a 4-byte TRNG number
        trng_bytes = trng(bytes_per_decimal)
        # Convert the bytes to a decimal value and write to file
        decimal_value = sum([b * 256**(bytes_per_decimal-j-1) for j, b in enumerate(trng_bytes)])
        f.write(str(decimal_value) + '\n')
