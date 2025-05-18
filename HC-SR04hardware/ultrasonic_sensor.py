import RPi.GPIO as GPIO
import time

TRIG = 5
ECHO = 6

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        end = time.time()

    duration = end - start
    distance = duration * 17150
    return distance

def is_obstacle_ahead():
    distance = get_distance()
    print(f"Distance: {distance:.2f} cm")
    return distance < 20  # cm
