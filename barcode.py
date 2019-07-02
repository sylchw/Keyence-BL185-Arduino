import RPi.GPIO as GPIO
import time
import serial

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

state = True

ser = serial.Serial(
        port=' /dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
#
#ser = serial.Serial ("/dev/ttyAMA0")    #Open named port 
#ser.baudrate = 9600                     #Set baud rate to 9600

mask = 0b01111111

while True:
    GPIO.output(18, True)
    time.sleep(0.1)
    
    c = ser.read()
    c = ord('a')
    result = c & mask
    print(result)
    
    GPIO.output(18,False)
    time.sleep(0.1)

