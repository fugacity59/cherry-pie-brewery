import RPi.GPIO as GPIO
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT) #pump 1
GPIO.setup(10, GPIO.OUT) #valve 1

GPIO.output(22, GPIO.HIGH)
GPIO.output(10, GPIO.HIGH)

print("start test")