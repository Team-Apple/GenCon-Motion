# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep
import wave
import jtalk
import sys
import get_talk_list

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
try:
    while True:
        if GPIO.input(18) == 1:
            talk_list = get_talk_list.get_talk_list()
            for talk in talk_list:
                jtalk.jtalk(talk)
                wf = wave.open("open_jtalk.wav", "r")
                sleep(float(wf.getnframes()) / wf.getframerate())
except KeyboardInterrupt:
    pass
GPIO.cleanup()
