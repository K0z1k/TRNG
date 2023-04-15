import os
import time
import struct
import numpy as np
import cv2
import imageio

#https://www.scopus.com/record/display.uri?eid=2-s2.0-70449470310&origin=resultslist&sort=plf-f&src=s&sid=db4296379cd4a73544e78d5087326eb2&sot=b&sdt=b&s=TITLE-ABS-KEY%28True+random+number+generators+on+PC%29&sl=45&sessionSearchId=db4296379cd4a73544e78d5087326eb2
#https://github.com/otms61/fortuna

capture = cv2.VideoCapture(0)

#tworzenie okna histogramu
hist_window = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('Histogram', cv2.WINDOW_NORMAL)

while True:
    ret, frame = capture.read()
    #cv2.imshow('Video', frame)
    
    
    #for i in buffer[1]:
    histogram = cv2.calcHist([frame], [0], None, [256], [0, 256])
    histogram = cv2.normalize(histogram, histogram, 0, 255, cv2.NORM_MINMAX)

    # Rysowanie histogramu na oknie
    hist_height = np.max(histogram)
    for i in range(256):
        intensity = int(histogram[i] * 300 / hist_height)
        cv2.line(hist_window, (i, 300), (i, 300 - intensity), (255, 255, 255))

    # Wyświetlanie histogramu
    cv2.imshow('Histogram', hist_window)



    buffer = cv2.imencode('.png', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()