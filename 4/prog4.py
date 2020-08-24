# Функции для RGB
def Green(r,g,b):
    pin.output(r,False)
    pin.output(g,True)
    pin.output(b,False)
    
def Red(r,g,b):
    pin.output(r,True)
    pin.output(g,False)
    pin.output(b,False)

def Blue(r,g,b):
    pin.output(r,False)
    pin.output(g,False)
    pin.output(b,True)

def Yellow(r,g,b):
    pin.output(r,True)
    pin.output(g,True)
    pin.output(b,False)

def Purple(r,g,b):
    pin.output(r,True)
    pin.output(g,False)
    pin.output(b,True)
    
def Indigo(r,g,b):
    pin.output(r,False)
    pin.output(g,True)
    pin.output(b,True)
    
def Orange(r,g,b):
    pin.output(r,True)
    pin.output(g,True)
    pin.output(b,False)

import RPi.GPIO as pin
import time
pin.cleanup()
pin.setmode(pin.BCM)

    
red = 17
green = 27
blue = 22

pin.setup(red,pin.OUT)
pin.setup(green,pin.OUT)
pin.setup(blue,pin.OUT)

while True:
    
    Red(red,green,blue)
    time.sleep(3)
    Orange(red,green,blue)
    time.sleep(3)
    Yellow(red,green,blue)
    time.sleep(3)
    Green(red,green,blue)
    time.sleep(3)
    Indigo(red,green,blue)
    time.sleep(3)
    Blue(red,green,blue)
    time.sleep(3)
    Purple(red,green,blue)
    time.sleep(3)

    
    

   
       
