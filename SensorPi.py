import RPi.GPIO as GPIO
import time
import random


class SensorPi:
    # Default constructor takes as parameter an id which is the sensor id
    # the cor is the corridor which it corresponds
    def __init__(self, id, corridor, pin_trigger, pin_echo):
        self.id = id
        self.corridor = corridor
        self.pin_trigger = pin_trigger
        self.pin_echo = pin_echo

    # def getDistance(self):
    # dist = 15
    # return dist

    # measures the distance from a sensor
    def calculateDistance(self):
         #return random.randint(1,50)
        try:
            GPIO.setmode(GPIO.BOARD)

            PIN_TRIGGER = self.pin_trigger
            PIN_ECHO = self.pin_echo

            GPIO.setup(PIN_TRIGGER, GPIO.OUT)
            GPIO.setup(PIN_ECHO, GPIO.IN)

            GPIO.output(PIN_TRIGGER, GPIO.LOW)
            print("Waiting for sensor to settle")

            time.sleep(0.1)

            print("Calculating distance")

            GPIO.output(PIN_TRIGGER, GPIO.HIGH)

            time.sleep(0.00001)

            GPIO.output(PIN_TRIGGER, GPIO.LOW)

            while GPIO.input(PIN_ECHO) == 0:
                pulse_start_time = time.time()
            while GPIO.input(PIN_ECHO) == 1:
                pulse_end_time = time.time()

            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)
            print("Distance:", distance, " cm")
            GPIO.setup(PIN_TRIGGER, GPIO.OUT)
            GPIO.setup(PIN_ECHO, GPIO.IN)

            GPIO.output(PIN_TRIGGER, GPIO.LOW)

            print("Waiting for sensor to settle")

            return distance

        finally:
            GPIO.cleanup()
