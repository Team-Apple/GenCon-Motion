# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep
import wave
import jtalk
import sys
import datetime
import json
import requests
import make_sentence

today = datetime.date.today()
url = 'https://gencon-web.herokuapp.com/api/events.json?start_at_date=' + str(today)
req = requests.get(url)
event_dic = json.loads(req.text)
print(event_dic)
if event_dic == []:
    print 'data is not exist.'

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

try:
	while True:
		if GPIO.input(18) == 1:
			mode = 'event'
			today = datetime.date.today()
			url = 'https://gencon-web.herokuapp.com/api/events.json?start_at_date=' + str(today)
			req = requests.get(url)
			event_dic = json.loads(req.text)
			print(event_dic)
			if event_dic == []:
			    print 'data is not exist.'
			for i in range(len(event_dic)):
				title = event_dic[i]['title']
				memo = event_dic[i]['memo']
				sentence = make_sentence.make_sentence(mode, title, memo)
				jtalk.jtalk(sentence)
				wf = wave.open("open_jtalk.wav", "r")
				sleep(float(wf.getnframes()) / wf.getframerate())
except KeyboardInterrupt:
	pass

GPIO.cleanup()
