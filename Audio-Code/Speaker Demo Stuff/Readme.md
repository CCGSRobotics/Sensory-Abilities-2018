# Speaker Code
**Last updated on 12/6/2018**

Welcome to the King's Legacy 2018 Speaker Code - an implementation of Python 3's pyaudio module using sockets and a callback function to ensure a smooth and clear transfer of live audio from one device to another.

This file serves as a documentation which explains:
* The User Guide
* Known issues and practical solutions
* How the Code is constructed
* Future plans to improve the code

Currently, this code has been written in a basic, low level manner and is considerably tedious to run. At some point it will be updated so that it will be easier to use.
## User Guide
**How to start the Pyaudio Server**
1. On the server side of the potential connection, run the code that is named "audioserver.py". The code should not output anything.
	- If the code complains about anything to do with ALSA, please ignore them.
	- As long as the code has not crashed, then everything is working correctly.
2. On the client side of the potential connection, run the code that is named "audioclient.py". The code should not output anything.
	- Please input the IP address of the server when asked.
	- If the code complains about anything to do with ALSA, please ignore them.
	- As long as the code has not crashed, then everything is working correctly.

At this point, you are all good to go!

## Known issues and practical solutions
1. The audio output is garbled (extremely unclear):
	- This is most likely because the internet connection between the client and the server is poor.
	- It is also possible that the microphone is spoilt or broken. In which needs to be checked with code that is not reliant on internt.
	- The speaker output is going back into the microphone (because they are close together) and is causing a loop. This may spoil both the speaker and the microphone.
	- The code has some overlooked bugs which MUST BE REPORTED IMMEDIATELY.

