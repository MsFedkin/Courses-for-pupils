class Segment:
    
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
        
