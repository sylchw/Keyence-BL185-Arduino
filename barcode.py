import RPi.GPIO as GPIO
import time
import serial

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

state = True

ser = serial.Serial(
        "/dev/ttyS0", #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)


mask = 0b01111111
#hex_mask = 0x10F447


while True:
    GPIO.output(18, True)
    time.sleep(0.1)
    
    message_list = []
    
    while ser.in_waiting:
        c = ser.read()
        convert_to_int = ord(c)
        result = convert_to_int & mask
        message_list.append(chr(result))
        #print(chr(result), end='')
        
    message = ''.join(message_list)
    print(message)
    print()
    GPIO.output(18,False)
    time.sleep(0.1)
