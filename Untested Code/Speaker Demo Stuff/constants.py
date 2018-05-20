# TCP Constants
import pyaudio

RATE = 48000
CHANNELS = 1
CHUNK_SIZE = 1024
WIDTH = pyaudio.paInt32

HOST = "127.0.0.1"
PORT = 12024

class AudioPlayer:
    """ Plays a single chunk of audio data """ 
    def __init__(self, chunksize, width, rate, channels):
        """ Init audio stream """ 
        self.p = pyaudio.PyAudio()

        self.audioData = "" # This is mutable
        self.chunksize = chunksize
        self.width = width
        self.rate = rate
        self.channels = channels

        self.stream = self.p.open(
            format = self.width,
            channels = self.channels,
            rate = self.rate,
            output = True
        )

    def play(self):
        """ Play entire BYTE STRING """
        self.stream.write(self.audioData)
        #print(len(self.audioData), end = "\n--------------------------\n")
        #for i in range(0,len(self.audioData),len(self.audioData)//self.chunksize):
            #print(self.audioData[i:i + (len(self.audioData)//self.chunksize)])
        #    self.stream.write(self.audioData[i:i + (len(self.audioData)//self.chunksize)])

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()
