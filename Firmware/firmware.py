from machine import Pin, ADC
import utime
from servo import Servo
from neopixel import Neopixel
import random

NUM_LEDS = 30
PIXEL_PIN = 0  # switch to real gpio pin
pixels = Neopixel(NUM_LEDS, 0, PIXEL_PIN, "RGBW")


# servo 1 needs to control the z spool, will go to 360 when button is pressed,
# wait a second and then go back to 0
servo1 = Servo(0)
# servo 2 needs to control the claw, so same movement as servo 1 (may be
# reversed)
servo2 = Servo(1)
# stepper 1 will run one way when joystick x is positive and the other way when
# negative
step1 = Pin(2, Pin.OUT)
dir1 = Pin(3, Pin.OUT)
# stepper 2 will run same as stepper 1 except for the y axis
step2 = Pin(4, Pin.OUT)
dir2 = Pin(5, Pin.OUT)
# map of where the claw is so motors don't go too far
# 0, 0 is the prize hole
xymap = [0, 0]
# placeholders for now
xlimit = 24
ylimit = 24

xAxis = ADC(Pin(26))
yAxis = ADC(Pin(27))
joystick_btn = Pin(16, Pin.IN, Pin.PULL_UP)
button = Pin(17, Pin.IN, Pin.PULL_UP)


def step_once(step_pin, dir_pin, direction, delay=0.001):
    dir_pin.value(direction)
    step_pin.high()
    utime.sleep(delay)
    step_pin.low()
    utime.sleep(delay)


def collect_prize(serv_1, serv_2):
    serv_1.move(360)  # spool
    serv_2.move(360)  # claw
    utime.sleep(0.5)
    serv_1.move(0)
    serv_2.move(0)


def goto_xy(stepA, stepB, dirA, dirB):
    print("ok")
    # this will depend heavily on the speed of the motors and the size of the
    # machine. Will finish later


def update_neopixels():
    colors = [[50, 0, 0, 25],  # pink
              [0, 20, 0, 25],  # light green
              [5, 0, 50, 25],  # blue
              [20, 25, 0, 25],  # yellow
              [0, 0, 5, 30]]  # white
    pixels.fill((colors[random.randint(1, 5)]))  # r, g, b, w
    pixels.show()


while True:
    # joystick
    x = xAxis.read_u16()
    y = yAxis.read_u16()
    btn_jstick = joystick_btn.value()
    btn = button.value()

    if btn == 1:
        collect_prize(servo1, servo2)
        goto_xy(step1, step2, dir1, dir2, 0, 0)
    if x > 0:
        step_once(step1, dir1, 1)
    elif x < 0:
        step_once(step1, dir1, 0)
    if y > 0:
        step_once(step2, dir2, 1)
    elif y < 0:
        step_once(step2, dir2, 0)
    # angle1 = int((x / 65535) * 360)
    # angle2 = int((y / 65535) * 360)

    utime.sleep(0.01)
