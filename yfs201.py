from machine import Pin, Timer
from time import sleep


yfr = Pin(32, Pin.IN)

np = 0 # Numero de pulsos

reload = Timer(0)

def pulseIn(pin):
    global np
    np += 1

def frequencyCheck(timer):
    global np, Q
    frec = np     
    Q = frec / 7.5    
    print (f"f= {frec} y Q= {Q}")
    print(yfr.value())
    np = 0  

print(yfr.value())

if(yfr.value() != 0) :
   yfr.irq(trigger = Pin.IRQ_RISING, handler = pulseIn)
   reload.init(mode= Timer.PERIODIC, period= 1000, callback= frequencyCheck)
   sleep(1)
