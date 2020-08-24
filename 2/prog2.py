import RPi.GPIO as pin
pin.cleanup()
pin.setmode(pin.BCM)
pin.setwarnings(False)

led = 17
button = 27


lastPush = False
permition = False


pin.setup(led,pin.OUT)
pin.setup(button,pin.IN)

while True:
    push = pin.input(button)
    
    if(push and not(lastPush)):
        permition = not permition
        pin.output(led,permition)
        
    push = lastPush
    
    
        
    


    