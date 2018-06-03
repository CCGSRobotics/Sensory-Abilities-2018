# TCP Constants
import pyaudio

RATE = 48000
CHANNELS = 1 # The pi microphone unfortunately has only one channel.
CHUNK_SIZE = 1024
WIDTH = pyaudio.paInt32 # If the interpreter cannot recognice what this constant is, then you have the wrong version of pyaudio.

HOST = "127.0.0.1" # Use this host if you are just relaying between two terminals on the same device.
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

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()
