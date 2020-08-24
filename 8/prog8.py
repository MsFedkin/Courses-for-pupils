class Segment:
    """
    Класс для управления семисегментного индикатора
    """
    
    def __init__(self,A,B,C,D,E,F,G):
        self.A = A;self.B = B;self.C = C
        self.D = D;self.E = E;self.F = F
        self.G = G
        # Настраиваем пины
        self.segments = [self.A,self.B,self.C,self.D,self.E,self.F,self.G]
        for i in self.segments:
            pin.setup(i,pin.OUT)
        
    
    def off(self):
        for i in self.segments:
            pin.output(i,False)
            
    def on(self):
        for i in self.segments:
            pin.output(i,True)
    
    def zero(self):
        for i in range(len(self.segments)-1):
            pin.output(self.segments,True)
            
        pin.output(self.G,False)
        
    def one(self):
        self.off()
        pin.output(self.B,True)
        pin.output(self.C,True)
    
    def two(self):
        self.on()
        pin.output(self.C,False)
        pin.output(self.F,False)
    
    def three(self):
        self.on()
        pin.output(self.E,False)
        pin.output(self.F,False)
        
    def four(self):
        self.on()
        pin.output(self.A,False)
        pin.output(self.E,False)
        pin.output(self.D,False)
    
    def five(self):
        self.on()
        pin.output(self.B,False)
        pin.output(self.E,False)
        
    def six(self):
        self.on()
        pin.output(self.B,False)
    
    def seven(self):
        self.off()
        pin.output(self.A,True)
        pin.output(self.B,True)
        pin.output(self.C,True)
    
    def eight(self):
        self.on()
    
    def nine(self):
        self.on()
        pin.output(self.E,False)
        
import RPi.GPIO as pin
from time import sleep 
pin.setmode(pin.BCM)

button = 9
pin.setup(button,pin.IN)

ss = Segment(2,3,4,17,27,22,10)

count = 0
"""
counter = {0 : ss.zero(),
           1 : ss.one(),
           2 : ss.two(),
           3 : ss.three(),
           4 : ss.four(),
           5 : ss.five(),
           6 : ss.six(),
           7 : ss.seven(),
           8 : ss.eight(),
           9 : ss.nine(),
           10 : ss.off()}
"""
while True:
    if pin.input(button):
        count +=1
        print(count)
    
    sleep(0.1)
    count = count % 11
    
    if(count == 0):
        ss.zero()
    if(count == 1):
        ss.one()
    if(count == 2):
        ss.two()
    if(count == 3):
        ss.three()
    if(count == 4):
        ss.four()
    if(count == 5):
        ss.five()
    if(count == 6):
        ss.six()
    if(count == 7):
        ss.seven()
    if(count == 8):
        ss.eight()
    if(count == 9):
        ss.nine()
    if(count == 10):
        ss.off()
    
    
    
    
    
    


