import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#4番のGPIOを入力ピンとして設定
GPIO.setup(4, GPIO.IN)
#4番のGPIOにTrueの入力があれば文字列を出力
if GPIO.input(4):
    print(”GPIO04:true”)
