import RPi.GPIO as GPIO
# GPIO pin numbers
switch = 4
led = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

flag = False

while True:
    while GPIO.input(switch):
        pass
    if flag:
        flag = False
    else:
        flag = True
    GPIO.output(led, flag)
