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
button = [10,9,11]

pin.setup(buzzer,pin.OUT)

for i in button:
    pin.setup(i,pin.IN)

melody = [262,523,784]

while True:
    t = 0
    for i in button:
        if pin.input(i):
            buzz(melody[t],0.5)
        t+=1
        






