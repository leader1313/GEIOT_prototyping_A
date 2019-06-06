import RPi.GPIO as GPIO
# GPIO pin numbers
switch = 4
led = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
while True:
    if GPIO.input(switch):
        GPIO.output(led, True)
    else:
        GPIO.output(led, False)
