#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib
import sys

def download():

    #送信先URL
    url = "https://api.voicetext.jp/v1/tts"
    #getパラメータ
    param = [
        ( "text", "text"),
        ( "speaker", "hikari"),
    ]

    urllib.urlretrieve(url,"?{0}".format( urllib.urlencode( param ))

if __name__ == "__main__":
    download()
