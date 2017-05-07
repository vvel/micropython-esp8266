import machine, time
from machine import Pin
th=0
tl=0
h=0
l=0
ppm=0
prevVal=0
redled=machine.Pin(0,machine.Pin.OUT)
blueled=machine.Pin(2,machine.Pin.OUT)
adc = machine.ADC(0)
pin = machine.Pin(5, Pin.IN)

t1=time.ticks_ms()
h=t1
l=t1
while True:
    i=pin.value()
    t1=time.ticks_ms()
    if ( i == 1):
        if (i != prevVal):
            h = t1
            tl = h - l
            prevVal = i
            #print("tl = " , tl)
    else:
         if (i != prevVal):
            l = t1
            th = l - h
            prevVal = i
            ppm = 5000 * (th - 2) / (th + tl - 4)
            #print("tl = " , tl,th)
            print("PPM = " , ppm, adc.read())
            #print(adc.read())
