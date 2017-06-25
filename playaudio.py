import pyaudio
import wave
import sys
import os

class Player:
    def __init__(self, file):
        self.file = file

    def play(self):
        os.system('aplay -D sysdefault:CARD=Device '+self.file)

    def close(self):
        os.system('killall -KILL aplay')
