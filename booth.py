#!/usr/bin/python

# import RPi.GPIO as GPIO
import os
import time

# Setup GPIO
phone = 18

def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(phone, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def startRecord():
    return

def endRecord():
    return

def playBeep():
    os.system('mpg123 -q beep.mp3 &')

def saveToCloud():
    return

def handlePickup():
    return

def handleHangup():
    return

def filename():
    return "call-"+str(time.time()).split('.')[0]+".wav"

def runBooth():
    try:
        while True:
            handlePickup()
            handleHangup()
    except KeyboardInterrupt:
        GPIO.cleanup()

## Setup booth
runBooth()
