#!/usr/bin/env python

import RPi.GPIO as GPIO
import os
import time
import playaudio as play
import recordaudio as record
import threading

# Setup audio
beep = play.Player('beep.wav')
recorder = record.Recorder()

def saveToCloud():
    return

def handlePickup():
    print('Picked up')
    time.sleep(1)
    beep.play()
    time.sleep(.2)
    recorder = record.Recorder()
    t = threading.Thread(target=recorder.startRecord)
    t.start()

def handleHangup():
    print('Hung up')
    recorder.endRecord()

def phoneState(channel):  
    if GPIO.input(18):
        handlePickup()
    else:
        handleHangup()

def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(18, GPIO.BOTH, callback=phoneState) 

def runBooth():
    print('ONE LAST CALL')
    setupGPIO()
    print('Booth online.')
    try:
        while True:
            time.sleep(0.2)
            
    except KeyboardInterrupt:
        GPIO.cleanup()
        beep.close()
        recorder.close()

## Setup booth
runBooth()
