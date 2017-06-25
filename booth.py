#!/usr/bin/env python

import RPi.GPIO as GPIO
import os
import time
import playaudio as play
import recordaudio as record
import threading

# Setup GPIO
phone = 18

# Setup audio
beep = play.Player('beep.wav')
recorder = record.Recorder()

def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(phone, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def saveToCloud():
    return

def handlePickup():
    print('Picked up')
    time.sleep(1)
    beep.play()
    recorder = record.Recorder()
    t = threading.Thread(target=recorder.startRecord)
    t.start()

def handleHangup():
    print('Hung up')
    recorder.endRecord()

def runBooth():
    print('ONE LAST CALL')
    setupGPIO()
    print('Booth online.')
    try:
        while True:
            if False:
                handlePickup()
            elif False:
                handleHangup()
    except KeyboardInterrupt:
        GPIO.cleanup()
        beep.close()
        recorder.close()

## Setup booth
runBooth()
