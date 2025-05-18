from hardware.ultrasonic_sensor import is_obstacle_ahead
from hardware.motor_driver import move_forward, stop, turn_left, turn_right
import time

def follow_path():
    path = ['forward', 'forward', 'right', 'forward', 'left', 'forward']
    for step in path:
        if is_obstacle_ahead():
            stop()
            print("Obstacle detected!")
            continue

        if step == 'forward':
            move_forward()
        elif step == 'left':
            turn_left()
        elif step == 'right':
            turn_right()

        time.sleep(2)
        stop()
