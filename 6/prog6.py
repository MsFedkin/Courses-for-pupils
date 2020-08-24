import RPi.GPIO as pin

pin.setmode(pin.BCM)
pin.setwarnings(False)

led = 17
ldr = 22
buzzer = 27

pin.setup(led,pin.OUT)
pin.setup(buzzer,pin.OUT)
pin.setup(ldr,pin.IN)

while True:
    lightness = int(pin.input(ldr)) * 422
    
    if lightness < 400:# Если яркость меньше 400 то сигналка срабатывает
        pin.output(led,True)
        pin.output(buzzer,True)
    else:
        pin.output(led,False)
        pin.output(buzzer,False)
    


