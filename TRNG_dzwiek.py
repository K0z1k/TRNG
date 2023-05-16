import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import keyboard
import scipy
import matplotlib
from ctypes import c_uint16 as unsigned_int16
from ctypes import c_uint8 as unsigned_int8

def audio(audio_samples = 50000000):

    CHUNK = 1024        
    FORMAT = pyaudio.paInt16  
    CHANNELS = 1     
    RATE = 44100    


    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)


    audio_data = []

    mask_a = 0b1111111100000000
    #mask_b = 0b0000000011111111
    
    print("Press 'q' to stop capturing audio...")
    while True:

        data = stream.read(CHUNK)
        temp = np.frombuffer(data, dtype=np.int16)
        #value0_10= 0
        for i in temp:
            a = abs(i)
            b = unsigned_int8(unsigned_int16((mask_b & i)<< 8))
            if(a != 0 and not(a >= 255)):
                if (a >= 0 and a < 50) and value0_10==6:
                    audio_data.append(a)
                    value0_10= 0
                elif (a >= 0 and a < 50) and value0_10 <6:
                    value0_10+=1
                else:
                    audio_data.append(a)
            if(b != 0 and b != 255):
                audio_data.append((b))


            

        if ((keyboard.is_pressed('q')) or (audio_samples <= len(audio_data))):
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    hist = plt.hist(audio_data,density=True,bins=256, range=[0, 255])
    matplotlib.pyplot.show()

    entropy = scipy.stats.entropy(hist[0],base = 2)



    print("Entropy: {}".format(entropy))


    
    #plt.show()
    #x = open("D:/Studia/SEM6/TRNG/wyniki_audio.txt","w")
    #for i in audio_data:
    #   x.write(str(i))
    return audio_data
