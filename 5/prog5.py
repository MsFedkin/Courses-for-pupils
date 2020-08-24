#Функция для базера
def buzz (noteFreq, duration):
    halveWaveTime = 1 / (noteFreq * 2)
    waves = int(duration * noteFreq)
    for i in range(waves):
       pin.output(buzzer, True)
       time.sleep(halveWaveTime)
       pin.output(buzzer, False)
       time.sleep(halveWaveTime)

import RPi.GPIO as pin
import time

pin.setmode(pin.BCM)
pin.setwarnings(False)

buzzer = 22
button = 27

pin.setup(buzzer,pin.OUT)
pin.setup(button,pin.IN)

melody = [262,196,196,220,196,1,247,262]
noteDuration = [0.25,0.125,0.125,0.25,0.25,0.25,0.25,0.25]

while True:
    if pin.input(button):
        t = 0
        for m in melody:
            buzz(m,noteDuration[t])
            time.sleep(noteDuration[t])
            t+=1

