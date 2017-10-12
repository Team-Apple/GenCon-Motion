# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep
import wave
import jtalk

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

try:
	while True:
		if GPIO.input(18) == 1:
			jtalk.jtalk("センサーだよ！")
			wf = wave.open("open_jtalk.wav", "r")
			sleep(float(wf.getnframes()) / wf.getframerate())

except KeyboardInterrupt:
	pass

GPIO.cleanup()
