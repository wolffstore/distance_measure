#!/usr/bin/python
import RPi.GPIO as GPIO
import time

class Measurer:
      #Default constructor takes as parameter an id which is the sensor id
      # the cor is the corridor which it corresponds
      def __init__(self,id,cor):
            self.id = id;
            self.cor = cor;

      #measures the distance from a sensor
      def measureDistance(self):
            dist = 0;
            try:
                  GPIO.setmode(GPIO.BOARD)

                  PIN_TRIGGER = 7
                  PIN_ECHO = 11

                  time.sleep(2)

                  print ("Calculating distance")

                  GPIO.output(PIN_TRIGGER, GPIO.HIGH)

                  time.sleep(0.00001)

                  GPIO.output(PIN_TRIGGER, GPIO.LOW)

                  while GPIO.input(PIN_ECHO)==0:
                        pulse_start_time = time.time()
                  while GPIO.input(PIN_ECHO)==1:
                        pulse_end_time = time.time()

                  pulse_duration = pulse_end_time - pulse_start_time
                  distance = round(pulse_duration * 17150, 2)
                  print ("Distance:",distance,"cm")
                  GPIO.setup(PIN_TRIGGER, GPIO.OUT)
                  GPIO.setup(PIN_ECHO, GPIO.IN)

                  GPIO.output(PIN_TRIGGER, GPIO.LOW)

                  print ("Waiting for sensor to settle")
                  dist = distance;
                  return dist;

            finally:
                  GPIO.cleanup()
