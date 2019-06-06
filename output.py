import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#4番のGPIOを出力ピンとして設定
GPIO.setup(4, GPIO.OUT)
#4番のGPIOをTrueにする
GPIO.output(4, True)
