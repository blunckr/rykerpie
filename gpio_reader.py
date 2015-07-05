import RPi.GPIO as GPIO
from time import sleep
from _connect_wiimotes import connect_wiimotes

GPIO.setmode(GPIO.BCM)

wiimote_button = 4
GPIO.setup(wiimote_button, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def connect_wiimotes_pressed(channel):
	connect_wiimotes()

GPIO.add_event_detect(wiimote_button, GPIO.FALLING, callback=connect_wiimotes_pressed, bouncetime=1000)

while True:
	sleep(1000)
