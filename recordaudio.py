import pyaudio
import wave
import time

class Recorder:
    CHUNK = 512
    FORMAT = pyaudio.paInt16 #paInt8
    CHANNELS = 1
    RATE = 44100 #sample rate
    WAVE_OUTPUT_FILENAME = "archive/call_"+str(int(time.time()))+time.strftime("_%I:%M%p_%d_%B_%Y.wav")

    def __init__(self):
        """ Init audio stream """ 
        self.audio = pyaudio.PyAudio()

        self.stream = self.audio.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK) #buffer

        self.frames = []
        self.recording = False


    def startRecord(self):
        """ Record audio entire file """
        print("* recording")
        
        self.recording = True
        self.frames = []

        while self.recording:
            try:
                data = self.stream.read(self.CHUNK)
            except IOError as ex:
                if ex[1] != pyaudio.paInputOverflowed:
                    raise
                data = '\x00' * self.CHUNK
            self.frames.append(data) # 2 bytes(16 bits) per channel

    def endRecord(self):
        """ Graceful shutdown """ 
        if(self.recording == True):
            print("* done recording")

            self.recording = False
            time.sleep(0.1)

            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()
        
            wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.audio.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(self.frames))
            wf.close()

    def close(self):
        """ Graceful shutdown """ 
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
