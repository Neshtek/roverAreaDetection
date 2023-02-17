import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Ultrasonic:
    def __init__(self, TRIGGER, ECHO):
        print('Created')
        self.TRIGGER = TRIGGER
        self.ECHO = ECHO
        self.driveOk = False
        self.areaCompleted = False
        GPIO.setup(self.TRIGGER, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)


    def getDistance(self):
        # set Trigger to HIGH
        GPIO.output(self.TRIGGER, True)
    
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.TRIGGER, False)
    
        StartTime = time.time()
        StopTime = time.time()
    
        # save StartTime
        while GPIO.input(self.ECHO) == 0:
            StartTime = time.time()
    
        # save time of arrival
        while GPIO.input(self.ECHO) == 1:
            StopTime = time.time()

        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34300) / 2
    
        if distance > 30:
            return 30
        else:
            return distance
    
    def checkDriveOk(self):
        edgeDist = self.getDistance()
        if edgeDist <= 10:
            return True
            print ("Measured Distance = %.1f cm" % edgeDist)
        else:
            return False
            print ("Measured Distance = %.1f cm" % edgeDist)
            time.sleep(1)
            dEdge = self.getDistance()
            if dEdge > 10:
                return False
                print ("Measured Distance 2 = %.1f cm" % dEdge)
            else:
                pass
        print ("Measured Distance = %.1f cm" % edgeDist)
        time.sleep(0.1)